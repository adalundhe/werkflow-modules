from pydantic import (
    BaseModel,
    StrictStr
)


class AWSs3DeleteObjectError(BaseModel):
    Key: StrictStr
    VersionId: StrictStr
    Code: StrictStr
    Message: StrictStr