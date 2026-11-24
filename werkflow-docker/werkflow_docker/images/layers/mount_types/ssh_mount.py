import re
from typing import Annotated, Any, Dict, Literal, Optional

from pydantic import BaseModel, StrictBool, StrictStr, StringConstraints


class SSHMount(BaseModel):
    mount_type: Literal['ssh'] = 'ssh'
    id: Optional[StrictStr] = None
    target: Optional[StrictStr] = None
    required: Optional[StrictBool] = None
    mode: Optional[
        Annotated[StrictStr, StringConstraints(max_length=4, pattern=r'^[0-7]*$')]
    ] = None
    user_id: Optional[StrictStr] = None
    group_id: Optional[StrictStr] = None

    def to_string(self) -> str:
        mount_string = f'--mount=type={self.mount_type}'

        if self.id:
            mount_string = f'{mount_string},id={self.id}'

        if self.target:
            mount_string = f'{mount_string},target={self.target}'

        if self.required is not None:
            required = 'true' if self.required else 'false'
            mount_string = f'{mount_string},required={required}'

        if self.mode:
            mount_string = f'{mount_string},mode={self.mode}'

        if self.user_id:
            mount_string = f'{mount_string},uid={self.user_id}'

        if self.group_id:
            mount_string = f'{mount_string},gid={self.group_id}'

        return mount_string

    @classmethod
    def parse(cls, line: str) -> 'SSHMount':
        options: Dict[str, Any] = {'mount_type': 'ssh'}
        tokens = [
            token.strip()
            for part in line.split(',')
            for token in part.split()
            if token.strip()
        ]

        for token in tokens:
            if token == 'required':
                options['required'] = True
            elif token.startswith('id='):
                options['id'] = token[len('id='):]
            elif token.startswith('target='):
                options['target'] = token[len('target='):]
            elif token.startswith('dst='):
                options['target'] = token[len('dst='):]
            elif token.startswith('required='):
                val = token[len('required='):].lower()
                options['required'] = val in ('true', '1')
            elif mode_match := re.fullmatch(r'mode=([0-7]{3,4})', token):
                options['mode'] = mode_match.group(1)
            elif uid_match := re.fullmatch(r'uid=([0-9]+)', token):
                options['user_id'] = uid_match.group(1)
            elif gid_match := re.fullmatch(r'gid=([0-9]+)', token):
                options['group_id'] = gid_match.group(1)

        return cls(**options)
