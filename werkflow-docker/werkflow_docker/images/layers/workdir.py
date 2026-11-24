import re
from typing import Literal

from pydantic import BaseModel, StrictStr


class Workdir(BaseModel):
    layer_type: Literal['workdir'] = 'workdir'
    path: StrictStr

    def to_string(self) -> str:
        return f'WORKDIR {self.path}'

    @classmethod
    def parse(cls, line: str) -> 'Workdir':
        stripped = re.sub(r'^WORKDIR\s+', '', line.strip(), count=1, flags=re.IGNORECASE).strip()
        return cls(path=stripped)
