from pydantic import (
    BaseModel,
    StrictStr
)


class BuildEnvar(BaseModel):
    name: StrictStr
    value: StrictStr

    def to_string(self):
        return f'{self.name}={self.value}'