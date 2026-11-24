from __future__ import annotations
from pydantic import BaseModel
from .auto_scaling_performance_factor_reference_request import AutoScalingPerformanceFactorReferenceRequest


class AutoScalingCpuPerformanceFactorRequest(BaseModel):
    References: list[AutoScalingPerformanceFactorReferenceRequest] | None = None
