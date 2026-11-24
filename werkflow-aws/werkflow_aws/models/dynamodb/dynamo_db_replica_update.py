from __future__ import annotations
from pydantic import BaseModel
from .dynamo_db_create_replica_action import DynamoDBCreateReplicaAction
from .dynamo_db_delete_replica_action import DynamoDBDeleteReplicaAction


class DynamoDBReplicaUpdate(BaseModel):
    Create: DynamoDBCreateReplicaAction | None = None
    Delete: DynamoDBDeleteReplicaAction | None = None
