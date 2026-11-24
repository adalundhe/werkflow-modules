from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .dms_filter import DMSFilter


class DMSDescribeDataMigrationsRequest(BaseModel):
    Filters: list[DMSFilter] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
    WithoutSettings: StrictBool | None = None
    WithoutStatistics: StrictBool | None = None
