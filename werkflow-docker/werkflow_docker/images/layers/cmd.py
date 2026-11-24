import json
import re
from typing import List, Literal, Union

from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class Cmd(BaseModel):
    layer_type: Literal['cmd'] = 'cmd'
    command: List[Union[StrictStr, StrictInt, StrictFloat, StrictBool]]

    def to_string(self) -> str:
        serialized = json.dumps([str(arg) for arg in self.command])
        return f'CMD {serialized}'

    @classmethod
    def parse(cls, line: str) -> 'Cmd':
        stripped = re.sub(r'^CMD\s+', '', line.strip(), count=1, flags=re.IGNORECASE).strip()

        if stripped.startswith('['):
            try:
                parsed = json.loads(stripped)
                if isinstance(parsed, list):
                    return cls(command=parsed)
            except json.JSONDecodeError:
                pass

            command: List[Union[str, int, float, bool]] = [
                arg.strip().strip('"').strip("'")
                for arg in re.sub(r'^\[|\]$', '', stripped).split(',')
                if arg.strip()
            ]
            return cls(command=command)

        return cls(command=[stripped] if stripped else [])
