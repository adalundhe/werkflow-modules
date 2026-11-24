from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel
from .ec2_vpc_encryption_control_exclusions import EC2VpcEncryptionControlExclusions


class EC2VpcEncryptionControl(BaseModel):
    VpcId: StrictStr | None = None
    VpcEncryptionControlId: StrictStr | None = None
    Mode: StrictStr | None = None
    State: StrictStr | None = None
    StateMessage: StrictStr | None = None
    ResourceExclusions: EC2VpcEncryptionControlExclusions | None = None
    Tags: list[EC2TagModel] | None = None
