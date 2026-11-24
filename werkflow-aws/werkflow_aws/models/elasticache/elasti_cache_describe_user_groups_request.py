from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ElastiCacheDescribeUserGroupsRequest(BaseModel):
    UserGroupId: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
