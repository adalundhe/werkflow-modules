from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MemoryDBDescribeParametersRequest(BaseModel):
    ParameterGroupName: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
