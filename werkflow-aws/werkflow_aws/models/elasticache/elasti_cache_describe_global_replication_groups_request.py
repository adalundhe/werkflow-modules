from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ElastiCacheDescribeGlobalReplicationGroupsRequest(BaseModel):
    GlobalReplicationGroupId: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
    ShowMemberInfo: StrictBool | None = None
