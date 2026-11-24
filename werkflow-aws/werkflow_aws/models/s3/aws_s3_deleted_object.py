from pydantic import (
    BaseModel,
    StrictBool,
    StrictStr,
)


class AWSs3DeletedObject(BaseModel):
    Key: StrictStr | None = None
    VersionId: StrictStr | None = None
    DeleteMarker: StrictBool | None = None
    DeleteMarkerVersionId: StrictStr | None = None
