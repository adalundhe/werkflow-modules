from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EFSDescribeAccessPointsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    AccessPointId: StrictStr | None = None
    FileSystemId: StrictStr | None = None
