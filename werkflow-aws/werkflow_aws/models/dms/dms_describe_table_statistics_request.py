from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dms_filter import DMSFilter


class DMSDescribeTableStatisticsRequest(BaseModel):
    ReplicationTaskArn: StrictStr
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
    Filters: list[DMSFilter] | None = None
