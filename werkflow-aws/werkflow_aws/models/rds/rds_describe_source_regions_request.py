from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .rds_filter_model import RDSFilterModel


class RDSDescribeSourceRegionsRequest(BaseModel):
    RegionName: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
    Filters: list[RDSFilterModel] | None = None
