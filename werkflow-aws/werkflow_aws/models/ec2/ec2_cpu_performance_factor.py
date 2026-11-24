from __future__ import annotations
from pydantic import BaseModel
from .ec2_performance_factor_reference import EC2PerformanceFactorReference


class EC2CpuPerformanceFactor(BaseModel):
    References: list[EC2PerformanceFactorReference] | None = None
