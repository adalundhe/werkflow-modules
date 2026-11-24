from __future__ import annotations
from pydantic import BaseModel
from .auto_scaling_cpu_performance_factor_request import AutoScalingCpuPerformanceFactorRequest


class AutoScalingBaselinePerformanceFactorsRequest(BaseModel):
    Cpu: AutoScalingCpuPerformanceFactorRequest | None = None
