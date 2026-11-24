from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_analysis_component import EC2AnalysisComponent


class EC2AnalysisLoadBalancerTarget(BaseModel):
    Address: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    Instance: EC2AnalysisComponent | None = None
    Port: StrictInt | None = None
