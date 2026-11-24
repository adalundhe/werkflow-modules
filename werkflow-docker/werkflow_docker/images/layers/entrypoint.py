import json
import re
from typing import List, Literal

from pydantic import BaseModel, StrictStr


class Entrypoint(BaseModel):
    layer_type: Literal['entrypoint'] = 'entrypoint'
    command: List[StrictStr]

    def to_string(self) -> str:
        serialized = json.dumps(list(self.command))
        return f'ENTRYPOINT {serialized}'

    @classmethod
    def parse(cls, line: str) -> 'Entrypoint':
        stripped = re.sub(
            r'^ENTRYPOINT\s+',
            '',
            line.strip(),
            count=1,
            flags=re.IGNORECASE,
        ).strip()

        if stripped.startswith('['):
            try:
                parsed = json.loads(stripped)
                if isinstance(parsed, list):
                    return cls(command=[str(item) for item in parsed])
            except json.JSONDecodeError:
                pass

            command = [
                arg.strip().strip('"').strip("'")
                for arg in re.sub(r'^\[|\]$', '', stripped).split(',')
                if arg.strip()
            ]
            return cls(command=command)

        return cls(command=[stripped] if stripped else [])
