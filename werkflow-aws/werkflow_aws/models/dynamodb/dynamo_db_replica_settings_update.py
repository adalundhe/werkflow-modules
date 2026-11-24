from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .dynamo_db_auto_scaling_settings_update import DynamoDBAutoScalingSettingsUpdate
from .dynamo_db_replica_global_secondary_index_settings_update import DynamoDBReplicaGlobalSecondaryIndexSettingsUpdate


class DynamoDBReplicaSettingsUpdate(BaseModel):
    RegionName: StrictStr
    ReplicaProvisionedReadCapacityUnits: StrictInt | None = None
    ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate: DynamoDBAutoScalingSettingsUpdate | None = None
    ReplicaGlobalSecondaryIndexSettingsUpdate: list[DynamoDBReplicaGlobalSecondaryIndexSettingsUpdate] | None = None
    ReplicaTableClass: Literal['STANDARD', 'STANDARD_INFREQUENT_ACCESS'] | None = None
