from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKStopTopicReassignmentRequest(BaseModel):
    ClusterArn: StrictStr
    TopicReassignmentOperationArn: StrictStr
