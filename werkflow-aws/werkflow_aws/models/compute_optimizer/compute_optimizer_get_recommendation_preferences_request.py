from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .compute_optimizer_scope import ComputeOptimizerScope


class ComputeOptimizerGetRecommendationPreferencesRequest(BaseModel):
    resourceType: Literal['Ec2Instance', 'AutoScalingGroup', 'EbsVolume', 'LambdaFunction', 'NotApplicable', 'EcsService', 'License', 'RdsDBInstance', 'AuroraDBClusterStorage', 'Idle']
    scope: ComputeOptimizerScope | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
