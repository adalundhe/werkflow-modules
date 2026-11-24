from __future__ import annotations
from pydantic import BaseModel
from .ec2_instance_application_status import EC2InstanceApplicationStatus


class EC2ApplicationStatusesResponseType(BaseModel):
    Instances: list[EC2InstanceApplicationStatus] | None = None
