from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dms_filter import DMSFilter


class DMSDescribeReplicationTableStatisticsRequest(BaseModel):
    ReplicationConfigArn: StrictStr
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
    Filters: list[DMSFilter] | None = None
