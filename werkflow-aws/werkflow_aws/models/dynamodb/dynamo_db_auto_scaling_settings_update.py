from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .dynamo_db_auto_scaling_policy_update import DynamoDBAutoScalingPolicyUpdate


class DynamoDBAutoScalingSettingsUpdate(BaseModel):
    MinimumUnits: StrictInt | None = None
    MaximumUnits: StrictInt | None = None
    AutoScalingDisabled: StrictBool | None = None
    AutoScalingRoleArn: StrictStr | None = None
    ScalingPolicyUpdate: DynamoDBAutoScalingPolicyUpdate | None = None
