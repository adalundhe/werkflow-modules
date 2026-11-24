from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MSKUpdateTopicRequest(BaseModel):
    ClusterArn: StrictStr
    TopicName: StrictStr
    Configs: StrictStr | None = None
    PartitionCount: StrictInt | None = None
