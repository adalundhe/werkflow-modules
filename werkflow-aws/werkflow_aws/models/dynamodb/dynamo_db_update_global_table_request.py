from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_replica_update import DynamoDBReplicaUpdate


class DynamoDBUpdateGlobalTableRequest(BaseModel):
    GlobalTableName: StrictStr
    ReplicaUpdates: list[DynamoDBReplicaUpdate]
