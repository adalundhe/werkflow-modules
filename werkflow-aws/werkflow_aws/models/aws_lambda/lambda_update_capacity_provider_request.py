from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_capacity_provider_scaling_config import LambdaCapacityProviderScalingConfig
from .lambda_capacity_provider_telemetry_config import LambdaCapacityProviderTelemetryConfig
from .lambda_propagate_tags import LambdaPropagateTags


class LambdaUpdateCapacityProviderRequest(BaseModel):
    CapacityProviderName: StrictStr
    CapacityProviderScalingConfig: LambdaCapacityProviderScalingConfig | None = None
    PropagateTags: LambdaPropagateTags | None = None
    TelemetryConfig: LambdaCapacityProviderTelemetryConfig | None = None
