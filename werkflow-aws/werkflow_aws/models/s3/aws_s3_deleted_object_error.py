from pydantic import (
    BaseModel,
    StrictStr,
)


class AWSs3DeleteObjectError(BaseModel):
    Key: StrictStr | None = None
    VersionId: StrictStr | None = None
    Code: StrictStr | None = None
    Message: StrictStr | None = None
