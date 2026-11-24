from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ElastiCacheDescribeEngineDefaultParametersRequest(BaseModel):
    CacheParameterGroupFamily: StrictStr
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
