from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EFSDescribeTagsRequest(BaseModel):
    FileSystemId: StrictStr
    MaxItems: StrictInt | None = None
    Marker: StrictStr | None = None
