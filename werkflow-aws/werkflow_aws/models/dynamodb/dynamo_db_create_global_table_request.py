from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_replica import DynamoDBReplica


class DynamoDBCreateGlobalTableRequest(BaseModel):
    GlobalTableName: StrictStr
    ReplicationGroup: list[DynamoDBReplica]
