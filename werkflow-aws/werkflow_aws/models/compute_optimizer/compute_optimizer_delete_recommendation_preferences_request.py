from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .compute_optimizer_scope import ComputeOptimizerScope


class ComputeOptimizerDeleteRecommendationPreferencesRequest(BaseModel):
    resourceType: Literal['Ec2Instance', 'AutoScalingGroup', 'EbsVolume', 'LambdaFunction', 'NotApplicable', 'EcsService', 'License', 'RdsDBInstance', 'AuroraDBClusterStorage', 'Idle']
    recommendationPreferenceNames: list[Literal['EnhancedInfrastructureMetrics', 'InferredWorkloadTypes', 'ExternalMetricsPreference', 'LookBackPeriodPreference', 'PreferredResources', 'UtilizationPreferences']]
    scope: ComputeOptimizerScope | None = None
