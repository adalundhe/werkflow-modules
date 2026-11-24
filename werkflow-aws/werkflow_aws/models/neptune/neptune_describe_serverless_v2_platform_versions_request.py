from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .neptune_filter import NeptuneFilter


class NeptuneDescribeServerlessV2PlatformVersionsRequest(BaseModel):
    ServerlessV2PlatformVersion: StrictStr | None = None
    Engine: StrictStr | None = None
    Filters: list[NeptuneFilter] | None = None
    DefaultOnly: StrictBool | None = None
    IncludeAll: StrictBool | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
