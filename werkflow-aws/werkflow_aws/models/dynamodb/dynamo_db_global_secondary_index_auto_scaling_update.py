from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_auto_scaling_settings_update import DynamoDBAutoScalingSettingsUpdate


class DynamoDBGlobalSecondaryIndexAutoScalingUpdate(BaseModel):
    IndexName: StrictStr | None = None
    ProvisionedWriteCapacityAutoScalingUpdate: DynamoDBAutoScalingSettingsUpdate | None = None
