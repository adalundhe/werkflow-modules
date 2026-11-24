import re
from typing import Annotated, Any, Dict, Literal, Optional

from pydantic import BaseModel, StrictBool, StrictStr, StringConstraints


class CacheMount(BaseModel):
    mount_type: Literal['cache'] = 'cache'
    id: Optional[StrictStr] = None
    target: StrictStr
    source: Optional[StrictStr] = None
    from_source: Optional[StrictStr] = None
    readonly: Optional[StrictBool] = None
    sharing: Optional[Literal['shared', 'private', 'locked']] = None
    mode: Optional[
        Annotated[StrictStr, StringConstraints(max_length=4, pattern=r'^[0-7]*$')]
    ] = None
    user_id: Optional[StrictStr] = None
    group_id: Optional[StrictStr] = None

    def to_string(self) -> str:
        mount_string = f'--mount=type={self.mount_type},target={self.target}'

        if self.id:
            mount_string = f'{mount_string},id={self.id}'

        if self.source:
            mount_string = f'{mount_string},source={self.source}'

        if self.from_source:
            mount_string = f'{mount_string},from={self.from_source}'

        if self.readonly is not None:
            readonly = 'true' if self.readonly else 'false'
            mount_string = f'{mount_string},readonly={readonly}'

        if self.sharing:
            mount_string = f'{mount_string},sharing={self.sharing}'

        if self.mode:
            mount_string = f'{mount_string},mode={self.mode}'

        if self.user_id:
            mount_string = f'{mount_string},uid={self.user_id}'

        if self.group_id:
            mount_string = f'{mount_string},gid={self.group_id}'

        return mount_string

    @classmethod
    def parse(cls, line: str) -> 'CacheMount':
        options: Dict[str, Any] = {'mount_type': 'cache'}
        tokens = [
            token.strip()
            for part in line.split(',')
            for token in part.split()
            if token.strip()
        ]

        for token in tokens:
            if token in ('readonly', 'ro'):
                options['readonly'] = True
            elif token in ('readwrite', 'rw'):
                options['readonly'] = False
            elif token.startswith('id='):
                options['id'] = token[len('id='):]
            elif token.startswith('target='):
                options['target'] = token[len('target='):]
            elif token.startswith('source='):
                options['source'] = token[len('source='):]
            elif token.startswith('src='):
                options['source'] = token[len('src='):]
            elif token.startswith('from='):
                options['from_source'] = token[len('from='):]
            elif token.startswith('readonly='):
                val = token[len('readonly='):].lower()
                options['readonly'] = val in ('true', '1')
            elif token.startswith('ro='):
                val = token[len('ro='):].lower()
                options['readonly'] = val in ('true', '1')
            elif token.startswith('sharing='):
                sharing_val = token[len('sharing='):]
                if sharing_val in ('shared', 'private', 'locked'):
                    options['sharing'] = sharing_val
            elif mode_match := re.fullmatch(r'mode=([0-7]{3,4})', token):
                options['mode'] = mode_match.group(1)
            elif uid_match := re.fullmatch(r'uid=([0-9]+)', token):
                options['user_id'] = uid_match.group(1)
            elif gid_match := re.fullmatch(r'gid=([0-9]+)', token):
                options['group_id'] = gid_match.group(1)

        return cls(**options)
