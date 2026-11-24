from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MemoryDBDescribeParameterGroupsRequest(BaseModel):
    ParameterGroupName: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
