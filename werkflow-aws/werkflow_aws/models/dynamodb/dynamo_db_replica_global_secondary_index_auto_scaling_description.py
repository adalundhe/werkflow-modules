from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_auto_scaling_settings_description import DynamoDBAutoScalingSettingsDescription


class DynamoDBReplicaGlobalSecondaryIndexAutoScalingDescription(BaseModel):
    IndexName: StrictStr | None = None
    IndexStatus: StrictStr | None = None
    ProvisionedReadCapacityAutoScalingSettings: DynamoDBAutoScalingSettingsDescription | None = None
    ProvisionedWriteCapacityAutoScalingSettings: DynamoDBAutoScalingSettingsDescription | None = None
