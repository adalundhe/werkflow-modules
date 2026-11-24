from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class MSKDescribeTopicResponse(BaseModel):
    TopicArn: StrictStr | None = None
    TopicName: StrictStr | None = None
    ReplicationFactor: StrictInt | None = None
    PartitionCount: StrictInt | None = None
    Configs: StrictStr | None = None
    Status: StrictStr | None = None
    ReplicaIds: list[StrictInt] | None = None
    ResponseMetadata: dict[str, Any] | None = None
