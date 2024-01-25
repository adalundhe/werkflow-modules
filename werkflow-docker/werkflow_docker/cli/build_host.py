from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt
)


class BuildHost(BaseModel):
    name: StrictStr
    host_ip: StrictStr
    host_port: StrictInt

    def to_string(self):
        return f'{self.name}={self.host_ip}:{self.host_port}'