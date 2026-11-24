from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_mac_system_integrity_protection_configuration import EC2MacSystemIntegrityProtectionConfiguration
from .ec2_tag_model import EC2TagModel


class EC2MacModificationTask(BaseModel):
    InstanceId: StrictStr | None = None
    MacModificationTaskId: StrictStr | None = None
    MacSystemIntegrityProtectionConfig: EC2MacSystemIntegrityProtectionConfiguration | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    TaskState: StrictStr | None = None
    TaskType: StrictStr | None = None
