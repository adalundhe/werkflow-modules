from __future__ import annotations
from pydantic import BaseModel
from .ec2_cpu_performance_factor import EC2CpuPerformanceFactor


class EC2BaselinePerformanceFactors(BaseModel):
    Cpu: EC2CpuPerformanceFactor | None = None
