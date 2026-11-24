import re
from typing import Literal

from pydantic import BaseModel, StrictStr


class Label(BaseModel):
    layer_type: Literal['label'] = 'label'
    name: StrictStr
    value: StrictStr

    def to_string(self) -> str:
        return f'LABEL {self.name}="{self.value}"'

    @classmethod
    def parse(cls, line: str) -> 'Label':
        stripped = re.sub(r'^LABEL\s+', '', line.strip(), count=1, flags=re.IGNORECASE).strip()
        name, value = stripped.split('=', 1)
        clean_value = value.strip()
        if (
            len(clean_value) >= 2
            and clean_value[0] == clean_value[-1]
            and clean_value[0] in ('"', "'")
        ):
            clean_value = clean_value[1:-1]

        return cls(
            name=name.strip(),
            value=clean_value,
        )
