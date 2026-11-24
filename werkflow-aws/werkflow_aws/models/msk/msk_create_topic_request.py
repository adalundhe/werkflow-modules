from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MSKCreateTopicRequest(BaseModel):
    ClusterArn: StrictStr
    TopicName: StrictStr
    PartitionCount: StrictInt
    ReplicationFactor: StrictInt
    Configs: StrictStr | None = None
