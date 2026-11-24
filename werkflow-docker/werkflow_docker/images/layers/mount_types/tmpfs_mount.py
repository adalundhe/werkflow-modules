import re
from typing import Any, Dict, Literal, Optional

from pydantic import BaseModel, StrictInt, StrictStr


class TMPFSMount(BaseModel):
    mount_type: Literal['tmpfs'] = 'tmpfs'
    target: StrictStr
    size: Optional[StrictInt] = None

    def to_string(self) -> str:
        mount_string = f'--mount=type={self.mount_type},target={self.target}'

        if self.size is not None:
            mount_string = f'{mount_string},size={self.size}'

        return mount_string

    @classmethod
    def parse(cls, line: str) -> 'TMPFSMount':
        options: Dict[str, Any] = {'mount_type': 'tmpfs'}

        tokens = [
            token.strip()
            for part in line.split(',')
            for token in part.split()
            if token.strip()
        ]

        for token in tokens:
            if token.startswith('target='):
                options['target'] = token[len('target='):]
            elif token.startswith('destination='):
                options['target'] = token[len('destination='):]
            elif token.startswith('dst='):
                options['target'] = token[len('dst='):]
            elif size := re.search(r'size=([0-9]+)', token):
                options['size'] = cls._match_size(size.group(0))

        return cls(**options)

    @classmethod
    def _match_size(cls, token: str) -> Optional[int]:
        if size := re.search(r'[0-9]+', token):
            return int(size.group(0))
        return None
