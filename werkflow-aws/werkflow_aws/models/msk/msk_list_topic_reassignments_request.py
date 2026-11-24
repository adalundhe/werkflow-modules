from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MSKListTopicReassignmentsRequest(BaseModel):
    ClusterArn: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    StatusFilter: StrictStr | None = None
