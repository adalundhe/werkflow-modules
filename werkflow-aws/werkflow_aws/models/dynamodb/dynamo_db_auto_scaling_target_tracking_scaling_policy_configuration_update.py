from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt


class DynamoDBAutoScalingTargetTrackingScalingPolicyConfigurationUpdate(BaseModel):
    TargetValue: StrictFloat | StrictInt
    DisableScaleIn: StrictBool | None = None
    ScaleInCooldown: StrictInt | None = None
    ScaleOutCooldown: StrictInt | None = None
