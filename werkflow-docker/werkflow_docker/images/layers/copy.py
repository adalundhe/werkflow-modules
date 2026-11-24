import re
from typing import Annotated, Any, Dict, List, Literal, Optional, Tuple, Union

from pydantic import (
    BaseModel,
    DirectoryPath,
    FilePath,
    StrictBool,
    StrictStr,
    StringConstraints,
)


class Copy(BaseModel):
    layer_type: Literal['copy'] = 'copy'
    source: Union[FilePath, DirectoryPath, StrictStr]
    destination: StrictStr
    user_id: Optional[StrictStr] = None
    group_id: Optional[StrictStr] = None
    permissions: Optional[
        Annotated[StrictStr, StringConstraints(max_length=4, pattern=r'^[0-7]*$')]
    ] = None
    from_source: Optional[StrictStr] = None
    link: StrictBool = False

    def to_string(self) -> str:
        copy_string = 'COPY'

        if self.user_id and self.group_id:
            copy_string = f'{copy_string} --chown={self.user_id}:{self.group_id}'
        elif self.user_id:
            copy_string = f'{copy_string} --chown={self.user_id}'

        if self.permissions:
            copy_string = f'{copy_string} --chmod={self.permissions}'

        if self.from_source:
            copy_string = f'{copy_string} --from={self.from_source}'

        if self.link:
            copy_string = f'{copy_string} --link'

        source_str = str(self.source)
        if not source_str.startswith(('/', './', '../')) and not self.from_source:
            source_str = f'./{source_str}'

        return f'{copy_string} {source_str} {self.destination}'

    @classmethod
    def parse(cls, line: str) -> 'Copy':
        stripped = re.sub(r'^COPY\s+', '', line.strip(), count=1, flags=re.IGNORECASE).strip()
        tokens = stripped.split()

        options: Dict[str, Any] = {}
        remainders: List[str] = []

        for token in tokens:
            if token == '--link':
                options['link'] = True
            elif token.startswith('--from='):
                options['from_source'] = token[len('--from='):]
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
            raise ValueError(f'Invalid COPY instruction: {line!r}')

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
