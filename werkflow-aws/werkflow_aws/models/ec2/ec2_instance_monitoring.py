from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_monitoring import EC2Monitoring


class EC2InstanceMonitoring(BaseModel):
    InstanceId: StrictStr | None = None
    Monitoring: EC2Monitoring | None = None
