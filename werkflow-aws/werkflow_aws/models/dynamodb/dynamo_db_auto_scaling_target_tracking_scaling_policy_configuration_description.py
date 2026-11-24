from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt


class DynamoDBAutoScalingTargetTrackingScalingPolicyConfigurationDescription(BaseModel):
    DisableScaleIn: StrictBool | None = None
    ScaleInCooldown: StrictInt | None = None
    ScaleOutCooldown: StrictInt | None = None
    TargetValue: StrictFloat | StrictInt | None = None
