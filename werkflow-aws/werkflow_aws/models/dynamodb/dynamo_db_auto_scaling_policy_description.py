from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_auto_scaling_target_tracking_scaling_policy_configuration_description import DynamoDBAutoScalingTargetTrackingScalingPolicyConfigurationDescription


class DynamoDBAutoScalingPolicyDescription(BaseModel):
    PolicyName: StrictStr | None = None
    TargetTrackingScalingPolicyConfiguration: DynamoDBAutoScalingTargetTrackingScalingPolicyConfigurationDescription | None = None
