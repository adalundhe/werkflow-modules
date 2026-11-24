from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .rds_filter_model import RDSFilterModel


class RDSDescribeOptionGroupsRequest(BaseModel):
    OptionGroupName: StrictStr | None = None
    Filters: list[RDSFilterModel] | None = None
    Marker: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    EngineName: StrictStr | None = None
    MajorEngineVersion: StrictStr | None = None
