import re
from typing import Any, Dict, Literal, Optional, Union

from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class Arg(BaseModel):
    layer_type: Literal['arg'] = 'arg'
    name: StrictStr
    default: Optional[Union[StrictStr, StrictInt, StrictBool, StrictFloat]] = None

    def to_string(self) -> str:
        default = self.default
        if default is not None:
            if isinstance(default, str):
                return f'ARG {self.name}="{default}"'
            return f'ARG {self.name}={default}'

        return f'ARG {self.name}'

    @classmethod
    def parse(cls, line: str) -> 'Arg':
        token = re.sub(r'^ARG\s+', '', line.strip(), count=1, flags=re.IGNORECASE).strip()

        options: Dict[str, Any] = {}

        if '=' in token:
            name, default = token.split('=', 1)
            default_val = default.strip()
            if (
                len(default_val) >= 2
                and default_val[0] == default_val[-1]
                and default_val[0] in ('"', "'")
            ):
                default_val = default_val[1:-1]
            options['name'] = name.strip()
            options['default'] = default_val
        else:
            options['name'] = token

        return cls(**options)
