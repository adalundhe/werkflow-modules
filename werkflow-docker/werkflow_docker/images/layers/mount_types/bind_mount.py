from typing import Any, Dict, Literal, Optional

from pydantic import BaseModel, StrictBool, StrictStr


class BindMount(BaseModel):
    mount_type: Literal['bind'] = 'bind'
    target: StrictStr
    source: Optional[StrictStr] = None
    from_source: Optional[StrictStr] = None
    readwrite: Optional[StrictBool] = None

    def to_string(self) -> str:
        mount_string = f'--mount=type={self.mount_type},target={self.target}'

        if self.source:
            mount_string = f'{mount_string},source={self.source}'

        if self.from_source:
            mount_string = f'{mount_string},from={self.from_source}'

        if self.readwrite is True:
            mount_string = f'{mount_string},readwrite'
        elif self.readwrite is False:
            mount_string = f'{mount_string},readonly'

        return mount_string

    @classmethod
    def parse(cls, line: str) -> 'BindMount':
        options: Dict[str, Any] = {'mount_type': 'bind'}
        tokens = [
            token.strip()
            for part in line.split(',')
            for token in part.split()
            if token.strip()
        ]

        for token in tokens:
            if token in ('readwrite', 'rw'):
                options['readwrite'] = True
            elif token in ('readonly', 'ro'):
                options['readwrite'] = False
            elif token.startswith('target='):
                options['target'] = token[len('target='):]
            elif token.startswith('destination='):
                options['target'] = token[len('destination='):]
            elif token.startswith('dst='):
                options['target'] = token[len('dst='):]
            elif token.startswith('source='):
                options['source'] = token[len('source='):]
            elif token.startswith('src='):
                options['source'] = token[len('src='):]
            elif token.startswith('from='):
                options['from_source'] = token[len('from='):]
            elif token.startswith('readwrite='):
                val = token[len('readwrite='):].lower()
                options['readwrite'] = val in ('true', '1')
            elif token.startswith('rw='):
                val = token[len('rw='):].lower()
                options['readwrite'] = val in ('true', '1')
            elif token.startswith('readonly='):
                val = token[len('readonly='):].lower()
                options['readwrite'] = val not in ('true', '1')
            elif token.startswith('ro='):
                val = token[len('ro='):].lower()
                options['readwrite'] = val not in ('true', '1')

        return cls(**options)
