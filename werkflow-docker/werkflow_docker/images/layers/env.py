import re
from typing import List, Literal, Optional

from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class Env(BaseModel):
    layer_type: Literal['env'] = 'env'
    keys: List[StrictStr]
    values: List[StrictStr | StrictInt | StrictBool | StrictFloat]

    def to_string(self) -> str:
        key_value_pairs: List[str] = []
        for key, value in zip(self.keys, self.values):
            if isinstance(value, str):
                formatted_value = f'"{value}"'
            else:
                formatted_value = str(value)

            key_value_pairs.append(f'{key}={formatted_value}')

        key_value_string = ' \\\n\t'.join(key_value_pairs)
        return f'ENV {key_value_string}'

    @classmethod
    def parse(cls, line: str) -> 'Env':
        stripped = re.sub(r'^ENV\s+', '', line.strip(), count=1, flags=re.IGNORECASE).strip()

        tokens = [
            token.strip('\\').strip()
            for token in stripped.split()
            if len(token.strip('\\').strip()) > 0
        ]

        keys: List[str] = []
        values: List[StrictStr | StrictInt | StrictBool | StrictFloat] = []

        last_name: Optional[str] = None

        for token in tokens:
            key: Optional[str] = None
            value: Optional[str] = None

            if '=' in token:
                key, value = token.split('=', 1)
                value = value.strip()
                if (
                    len(value) >= 2
                    and value[0] == value[-1]
                    and value[0] in ('"', "'")
                ):
                    value = value[1:-1]
                last_name = None
            elif last_name is None:
                last_name = token.strip()
            else:
                key = last_name
                value = token.strip()
                if (
                    len(value) >= 2
                    and value[0] == value[-1]
                    and value[0] in ('"', "'")
                ):
                    value = value[1:-1]
                last_name = None

            if key is not None and value is not None:
                keys.append(key.strip())
                values.append(value)

        return cls(keys=keys, values=values)
