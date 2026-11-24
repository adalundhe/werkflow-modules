from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_auto_scaling_settings_update import DynamoDBAutoScalingSettingsUpdate
from .dynamo_db_global_secondary_index_auto_scaling_update import DynamoDBGlobalSecondaryIndexAutoScalingUpdate
from .dynamo_db_replica_auto_scaling_update import DynamoDBReplicaAutoScalingUpdate


class DynamoDBUpdateTableReplicaAutoScalingRequest(BaseModel):
    TableName: StrictStr
    GlobalSecondaryIndexUpdates: list[DynamoDBGlobalSecondaryIndexAutoScalingUpdate] | None = None
    ProvisionedWriteCapacityAutoScalingUpdate: DynamoDBAutoScalingSettingsUpdate | None = None
    ReplicaUpdates: list[DynamoDBReplicaAutoScalingUpdate] | None = None
