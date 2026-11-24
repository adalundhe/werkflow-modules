from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EFSDescribeMountTargetsRequest(BaseModel):
    MaxItems: StrictInt | None = None
    Marker: StrictStr | None = None
    FileSystemId: StrictStr | None = None
    MountTargetId: StrictStr | None = None
    AccessPointId: StrictStr | None = None
