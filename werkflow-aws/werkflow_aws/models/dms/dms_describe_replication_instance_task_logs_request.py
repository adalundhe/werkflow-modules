from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DMSDescribeReplicationInstanceTaskLogsRequest(BaseModel):
    ReplicationInstanceArn: StrictStr
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
