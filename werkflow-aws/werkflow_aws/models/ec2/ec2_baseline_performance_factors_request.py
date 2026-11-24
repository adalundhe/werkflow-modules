from __future__ import annotations
from pydantic import BaseModel
from .ec2_cpu_performance_factor_request import EC2CpuPerformanceFactorRequest


class EC2BaselinePerformanceFactorsRequest(BaseModel):
    Cpu: EC2CpuPerformanceFactorRequest | None = None
