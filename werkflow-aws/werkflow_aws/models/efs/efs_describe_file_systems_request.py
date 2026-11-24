from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EFSDescribeFileSystemsRequest(BaseModel):
    MaxItems: StrictInt | None = None
    Marker: StrictStr | None = None
    CreationToken: StrictStr | None = None
    FileSystemId: StrictStr | None = None
