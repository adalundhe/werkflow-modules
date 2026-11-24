from __future__ import annotations
from pydantic import BaseModel
from .ec2_performance_factor_reference_request import EC2PerformanceFactorReferenceRequest


class EC2CpuPerformanceFactorRequest(BaseModel):
    References: list[EC2PerformanceFactorReferenceRequest] | None = None
