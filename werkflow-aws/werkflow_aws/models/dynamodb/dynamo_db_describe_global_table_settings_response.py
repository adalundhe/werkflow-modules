from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dynamo_db_replica_settings_description import DynamoDBReplicaSettingsDescription


class DynamoDBDescribeGlobalTableSettingsResponse(BaseModel):
    GlobalTableName: StrictStr | None = None
    ReplicaSettings: list[DynamoDBReplicaSettingsDescription] | None = None
    ResponseMetadata: dict[str, Any] | None = None
