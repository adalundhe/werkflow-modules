from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dms_filter import DMSFilter


class DMSDescribeReplicationSubnetGroupsRequest(BaseModel):
    Filters: list[DMSFilter] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
