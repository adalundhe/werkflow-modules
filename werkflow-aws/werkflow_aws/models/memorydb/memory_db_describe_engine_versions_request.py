from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class MemoryDBDescribeEngineVersionsRequest(BaseModel):
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    ParameterGroupFamily: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    DefaultOnly: StrictBool | None = None
