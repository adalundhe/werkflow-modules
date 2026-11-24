from typing import Optional

from pydantic import BaseModel, StrictInt, StrictStr


class BuildHost(BaseModel):
    name: StrictStr
    host_ip: StrictStr
    host_port: Optional[StrictInt] = None

    def to_string(self) -> str:
        return f'{self.name}:{self.host_ip}'
