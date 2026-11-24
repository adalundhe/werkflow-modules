from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKDescribeTopicReassignmentRequest(BaseModel):
    ClusterArn: StrictStr
    TopicReassignmentOperationArn: StrictStr
