from pydantic import (
    BaseModel,
    StrictStr
)


class BuildCacheImage(BaseModel):
    name: StrictStr
    tag: StrictStr

    def to_string(self):
        return f'{self.name}:{self.tag}'