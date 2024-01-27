from pydantic import (
    BaseModel,
    StrictStr,
    StrictBool
)


class AWSs3DeletedObject(BaseModel):
    Key: StrictStr
    VersionId: StrictStr
    DeleteMarker: StrictBool
    DeleteMarkerVersionId: StrictStr
    