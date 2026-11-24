from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DevOpsGuruListAnomalousLogGroupsRequest(BaseModel):
    InsightId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
