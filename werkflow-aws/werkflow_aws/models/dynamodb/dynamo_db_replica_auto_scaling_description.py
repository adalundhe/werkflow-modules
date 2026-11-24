from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_auto_scaling_settings_description import DynamoDBAutoScalingSettingsDescription
from .dynamo_db_replica_global_secondary_index_auto_scaling_description import DynamoDBReplicaGlobalSecondaryIndexAutoScalingDescription


class DynamoDBReplicaAutoScalingDescription(BaseModel):
    RegionName: StrictStr | None = None
    GlobalSecondaryIndexes: list[DynamoDBReplicaGlobalSecondaryIndexAutoScalingDescription] | None = None
    ReplicaProvisionedReadCapacityAutoScalingSettings: DynamoDBAutoScalingSettingsDescription | None = None
    ReplicaProvisionedWriteCapacityAutoScalingSettings: DynamoDBAutoScalingSettingsDescription | None = None
    ReplicaStatus: StrictStr | None = None
