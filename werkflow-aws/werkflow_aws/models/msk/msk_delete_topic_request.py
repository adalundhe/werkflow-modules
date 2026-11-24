from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKDeleteTopicRequest(BaseModel):
    ClusterArn: StrictStr
    TopicName: StrictStr
