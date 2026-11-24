from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_table_statistics import DMSTableStatistics


class DMSDescribeReplicationTableStatisticsResponse(BaseModel):
    ReplicationConfigArn: StrictStr | None = None
    Marker: StrictStr | None = None
    ReplicationTableStatistics: list[DMSTableStatistics] | None = None
    ResponseMetadata: dict[str, Any] | None = None
