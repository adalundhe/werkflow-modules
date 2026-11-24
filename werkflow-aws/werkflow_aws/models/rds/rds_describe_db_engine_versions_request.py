from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_filter_model import RDSFilterModel


class RDSDescribeDBEngineVersionsRequest(BaseModel):
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    DBParameterGroupFamily: StrictStr | None = None
    Filters: list[RDSFilterModel] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
    DefaultOnly: StrictBool | None = None
    ListSupportedCharacterSets: StrictBool | None = None
    ListSupportedTimezones: StrictBool | None = None
    IncludeAll: StrictBool | None = None
