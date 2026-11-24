from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKStartTopicReassignmentRequest(BaseModel):
    ClusterArn: StrictStr
    TargetInstanceType: StrictStr
    TopicsToInclude: list[StrictStr]
    ClientToken: StrictStr | None = None
    TopicsToExclude: list[StrictStr] | None = None
