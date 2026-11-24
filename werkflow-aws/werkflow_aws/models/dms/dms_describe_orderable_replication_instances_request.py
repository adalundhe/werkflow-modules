from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DMSDescribeOrderableReplicationInstancesRequest(BaseModel):
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
