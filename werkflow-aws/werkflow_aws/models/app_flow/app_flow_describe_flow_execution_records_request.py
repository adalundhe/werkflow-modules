from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppFlowDescribeFlowExecutionRecordsRequest(BaseModel):
    flowName: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
