from pydantic import (
    BaseModel,
    StrictStr
)


class BuildLabel(BaseModel):
    name: StrictStr
    value: StrictStr

    def to_string(self):
        return f'{self.name}={self.value}'