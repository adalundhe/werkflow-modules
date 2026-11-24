from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .compute_optimizer_effective_preferred_resource import ComputeOptimizerEffectivePreferredResource
from .compute_optimizer_external_metrics_preference import ComputeOptimizerExternalMetricsPreference
from .compute_optimizer_instance_savings_estimation_mode import ComputeOptimizerInstanceSavingsEstimationMode
from .compute_optimizer_utilization_preference import ComputeOptimizerUtilizationPreference


class ComputeOptimizerEffectiveRecommendationPreferences(BaseModel):
    cpuVendorArchitectures: list[StrictStr] | None = None
    enhancedInfrastructureMetrics: StrictStr | None = None
    inferredWorkloadTypes: StrictStr | None = None
    externalMetricsPreference: ComputeOptimizerExternalMetricsPreference | None = None
    lookBackPeriod: StrictStr | None = None
    utilizationPreferences: list[ComputeOptimizerUtilizationPreference] | None = None
    preferredResources: list[ComputeOptimizerEffectivePreferredResource] | None = None
    savingsEstimationMode: ComputeOptimizerInstanceSavingsEstimationMode | None = None
