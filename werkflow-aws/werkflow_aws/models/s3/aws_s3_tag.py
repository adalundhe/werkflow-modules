from pydantic import (
    BaseModel,
    StrictStr,
)


class AWSs3Tag(BaseModel):
    Key: StrictStr
    Value: StrictStr
