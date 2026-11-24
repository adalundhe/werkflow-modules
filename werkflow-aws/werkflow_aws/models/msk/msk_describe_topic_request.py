from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKDescribeTopicRequest(BaseModel):
    ClusterArn: StrictStr
    TopicName: StrictStr
