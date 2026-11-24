from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_instance_status_details import EC2InstanceStatusDetails


class EC2InstanceStatusSummary(BaseModel):
    Details: list[EC2InstanceStatusDetails] | None = None
    Status: StrictStr | None = None
