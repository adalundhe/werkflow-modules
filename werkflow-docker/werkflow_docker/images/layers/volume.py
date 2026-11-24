import json
import re
from typing import Annotated, List, Literal

from pydantic import BaseModel, Field, StrictStr


class Volume(BaseModel):
    layer_type: Literal['volume'] = 'volume'
    paths: Annotated[List[StrictStr], Field(min_length=1)]

    def to_string(self) -> str:
        return f'VOLUME {json.dumps(list(self.paths))}'

    @classmethod
    def parse(cls, line: str) -> 'Volume':
        stripped = re.sub(r'^VOLUME\s+', '', line.strip(), count=1, flags=re.IGNORECASE).strip()

        paths: List[str] = []
        if stripped.startswith('['):
            try:
                parsed = json.loads(stripped)
                if isinstance(parsed, list):
                    paths = [str(item) for item in parsed]
            except json.JSONDecodeError:
                pass

            if not paths:
                paths = [
                    arg.strip().strip('"').strip("'")
                    for arg in re.sub(r'^\[|\]$', '', stripped).split(',')
                    if arg.strip()
                ]
        else:
            paths = stripped.split()

        return cls(paths=paths)
