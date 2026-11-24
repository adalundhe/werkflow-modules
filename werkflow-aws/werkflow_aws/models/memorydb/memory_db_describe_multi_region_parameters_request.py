from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MemoryDBDescribeMultiRegionParametersRequest(BaseModel):
    MultiRegionParameterGroupName: StrictStr
    Source: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
