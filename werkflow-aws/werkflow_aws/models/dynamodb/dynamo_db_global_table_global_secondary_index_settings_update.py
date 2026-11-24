from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dynamo_db_auto_scaling_settings_update import DynamoDBAutoScalingSettingsUpdate


class DynamoDBGlobalTableGlobalSecondaryIndexSettingsUpdate(BaseModel):
    IndexName: StrictStr
    ProvisionedWriteCapacityUnits: StrictInt | None = None
    ProvisionedWriteCapacityAutoScalingSettingsUpdate: DynamoDBAutoScalingSettingsUpdate | None = None
