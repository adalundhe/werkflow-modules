from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .neptune_filter import NeptuneFilter


class NeptuneDescribeEngineDefaultParametersRequest(BaseModel):
    DBParameterGroupFamily: StrictStr
    Filters: list[NeptuneFilter] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
