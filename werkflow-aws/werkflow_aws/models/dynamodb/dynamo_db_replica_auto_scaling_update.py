from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_auto_scaling_settings_update import DynamoDBAutoScalingSettingsUpdate
from .dynamo_db_replica_global_secondary_index_auto_scaling_update import DynamoDBReplicaGlobalSecondaryIndexAutoScalingUpdate


class DynamoDBReplicaAutoScalingUpdate(BaseModel):
    RegionName: StrictStr
    ReplicaGlobalSecondaryIndexUpdates: list[DynamoDBReplicaGlobalSecondaryIndexAutoScalingUpdate] | None = None
    ReplicaProvisionedReadCapacityAutoScalingUpdate: DynamoDBAutoScalingSettingsUpdate | None = None
