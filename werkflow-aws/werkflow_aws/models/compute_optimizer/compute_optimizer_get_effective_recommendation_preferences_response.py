from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .compute_optimizer_effective_preferred_resource import ComputeOptimizerEffectivePreferredResource
from .compute_optimizer_external_metrics_preference import ComputeOptimizerExternalMetricsPreference
from .compute_optimizer_utilization_preference import ComputeOptimizerUtilizationPreference


class ComputeOptimizerGetEffectiveRecommendationPreferencesResponse(BaseModel):
    enhancedInfrastructureMetrics: StrictStr | None = None
    externalMetricsPreference: ComputeOptimizerExternalMetricsPreference | None = None
    lookBackPeriod: StrictStr | None = None
    utilizationPreferences: list[ComputeOptimizerUtilizationPreference] | None = None
    preferredResources: list[ComputeOptimizerEffectivePreferredResource] | None = None
    ResponseMetadata: dict[str, Any] | None = None
