from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MSKTopicInfo(BaseModel):
    TopicArn: StrictStr | None = None
    TopicName: StrictStr | None = None
    ReplicationFactor: StrictInt | None = None
    PartitionCount: StrictInt | None = None
    OutOfSyncReplicaCount: StrictInt | None = None
    ReplicaIds: list[StrictInt] | None = None
