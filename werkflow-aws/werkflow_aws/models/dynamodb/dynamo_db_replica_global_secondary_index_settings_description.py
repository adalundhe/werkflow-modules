from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dynamo_db_auto_scaling_settings_description import DynamoDBAutoScalingSettingsDescription


class DynamoDBReplicaGlobalSecondaryIndexSettingsDescription(BaseModel):
    IndexName: StrictStr | None = None
    IndexStatus: StrictStr | None = None
    ProvisionedReadCapacityUnits: StrictInt | None = None
    ProvisionedReadCapacityAutoScalingSettings: DynamoDBAutoScalingSettingsDescription | None = None
    ProvisionedWriteCapacityUnits: StrictInt | None = None
    ProvisionedWriteCapacityAutoScalingSettings: DynamoDBAutoScalingSettingsDescription | None = None
