from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dynamo_db_auto_scaling_settings_update import DynamoDBAutoScalingSettingsUpdate


class DynamoDBReplicaGlobalSecondaryIndexSettingsUpdate(BaseModel):
    IndexName: StrictStr
    ProvisionedReadCapacityUnits: StrictInt | None = None
    ProvisionedReadCapacityAutoScalingSettingsUpdate: DynamoDBAutoScalingSettingsUpdate | None = None
