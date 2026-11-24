import re
from typing import Literal, Union

from pydantic import BaseModel, StrictInt, StrictStr


class StopSignal(BaseModel):
    layer_type: Literal['stopsignal'] = 'stopsignal'
    signal: Union[StrictStr, StrictInt]

    def to_string(self) -> str:
        return f'STOPSIGNAL {self.signal}'

    @classmethod
    def parse(cls, line: str) -> 'StopSignal':
        stripped = re.sub(
            r'^STOPSIGNAL\s+',
            '',
            line.strip(),
            count=1,
            flags=re.IGNORECASE,
        ).strip()

        if stripped.isdigit():
            return cls(signal=int(stripped))

        return cls(signal=stripped)
