from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_replica_auto_scaling_description import DynamoDBReplicaAutoScalingDescription


class DynamoDBTableAutoScalingDescription(BaseModel):
    TableName: StrictStr | None = None
    TableStatus: StrictStr | None = None
    Replicas: list[DynamoDBReplicaAutoScalingDescription] | None = None
