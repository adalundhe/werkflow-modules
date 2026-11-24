import re
from typing import Annotated, Any, Dict, List, Literal, Optional, Tuple

from pydantic import BaseModel, StrictBool, StrictStr, StringConstraints


class Add(BaseModel):
    layer_type: Literal['add'] = 'add'
    source: StrictStr
    destination: StrictStr
    user_id: Optional[StrictStr] = None
    group_id: Optional[StrictStr] = None
    permissions: Optional[
        Annotated[StrictStr, StringConstraints(max_length=4, pattern=r'^[0-7]*$')]
    ] = None
    checksum: Optional[StrictStr] = None
    link: StrictBool = False

    def to_string(self) -> str:
        add_string = 'ADD'

        if self.user_id and self.group_id:
            add_string = f'{add_string} --chown={self.user_id}:{self.group_id}'
        elif self.user_id:
            add_string = f'{add_string} --chown={self.user_id}'

        if self.permissions:
            add_string = f'{add_string} --chmod={self.permissions}'

        if self.checksum:
            add_string = f'{add_string} --checksum={self.checksum}'

        if self.link:
            add_string = f'{add_string} --link'

        return f'{add_string} {self.source} {self.destination}'

    @classmethod
    def parse(cls, line: str) -> 'Add':
        stripped = re.sub(r'^ADD\s+', '', line.strip(), count=1, flags=re.IGNORECASE).strip()
        tokens = stripped.split()

        options: Dict[str, Any] = {}
        remainders: List[str] = []

        for token in tokens:
            if token == '--link':
                options['link'] = True
            elif token.startswith('--checksum='):
                options['checksum'] = token[len('--checksum='):]
            elif token.startswith('--chmod='):
                options['permissions'] = token[len('--chmod='):]
            elif token.startswith('--chown='):
                chown_value = token[len('--chown='):]
                user_id, group_id = cls._match_ownership(chown_value)
                options['user_id'] = user_id
                options['group_id'] = group_id
            else:
                remainders.append(token)

        if len(remainders) < 2:
            raise ValueError(f'Invalid ADD instruction: {line!r}')

        destination = remainders[-1]
        source = ' '.join(remainders[:-1])

        return cls(
            source=source,
            destination=destination,
            **options,
        )

    @classmethod
    def _match_ownership(cls, token: str) -> Tuple[str, Optional[str]]:
        if ':' in token:
            user_id, group_id = token.split(':', 1)
            return user_id, group_id
        return token, None
