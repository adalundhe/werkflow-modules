from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .compute_optimizer_external_metrics_preference import ComputeOptimizerExternalMetricsPreference
from .compute_optimizer_preferred_resource import ComputeOptimizerPreferredResource
from .compute_optimizer_scope import ComputeOptimizerScope
from .compute_optimizer_utilization_preference import ComputeOptimizerUtilizationPreference


class ComputeOptimizerPutRecommendationPreferencesRequest(BaseModel):
    resourceType: Literal['Ec2Instance', 'AutoScalingGroup', 'EbsVolume', 'LambdaFunction', 'NotApplicable', 'EcsService', 'License', 'RdsDBInstance', 'AuroraDBClusterStorage', 'Idle']
    scope: ComputeOptimizerScope | None = None
    enhancedInfrastructureMetrics: Literal['Active', 'Inactive'] | None = None
    inferredWorkloadTypes: Literal['Active', 'Inactive'] | None = None
    externalMetricsPreference: ComputeOptimizerExternalMetricsPreference | None = None
    lookBackPeriod: Literal['DAYS_14', 'DAYS_32', 'DAYS_93'] | None = None
    utilizationPreferences: list[ComputeOptimizerUtilizationPreference] | None = None
    preferredResources: list[ComputeOptimizerPreferredResource] | None = None
    savingsEstimationMode: Literal['AfterDiscounts', 'BeforeDiscounts'] | None = None
