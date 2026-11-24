from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_replica import DynamoDBReplica


class DynamoDBGlobalTable(BaseModel):
    GlobalTableName: StrictStr | None = None
    ReplicationGroup: list[DynamoDBReplica] | None = None
