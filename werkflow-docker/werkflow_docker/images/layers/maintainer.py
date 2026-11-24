import re
from typing import Literal

from pydantic import BaseModel, StrictStr


class Maintainer(BaseModel):
    layer_type: Literal['maintainer'] = 'maintainer'
    author: StrictStr

    def to_string(self) -> str:
        return f'MAINTAINER {self.author}'

    @classmethod
    def parse(cls, line: str) -> 'Maintainer':
        author = re.sub(r'^MAINTAINER\s+', '', line.strip(), count=1, flags=re.IGNORECASE).strip()
        return cls(author=author)
