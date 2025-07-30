from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaTag(BaseModel):
    Key: StrictStr
    Value: StrictStr