from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MemoryDBDescribeMultiRegionParameterGroupsRequest(BaseModel):
    MultiRegionParameterGroupName: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
