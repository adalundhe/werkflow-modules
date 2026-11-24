from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_filter_model import RDSFilterModel


class RDSDescribeServerlessV2PlatformVersionsRequest(BaseModel):
    ServerlessV2PlatformVersion: StrictStr | None = None
    Engine: StrictStr | None = None
    Filters: list[RDSFilterModel] | None = None
    DefaultOnly: StrictBool | None = None
    IncludeAll: StrictBool | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
