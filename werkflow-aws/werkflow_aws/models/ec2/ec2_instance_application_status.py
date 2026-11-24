from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_application_status import EC2ApplicationStatus
from .ec2_tag_model import EC2TagModel


class EC2InstanceApplicationStatus(BaseModel):
    InstanceId: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    ApplicationStatus: EC2ApplicationStatus | None = None
    Tags: list[EC2TagModel] | None = None
