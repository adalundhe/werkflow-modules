from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .rds_filter_model import RDSFilterModel


class RDSDescribeDBProxyTargetGroupsRequest(BaseModel):
    DBProxyName: StrictStr
    TargetGroupName: StrictStr | None = None
    Filters: list[RDSFilterModel] | None = None
    Marker: StrictStr | None = None
    MaxRecords: StrictInt | None = None
