from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_account_vpc_encryption_control_exclusions import EC2AccountVpcEncryptionControlExclusions


class EC2AccountVpcEncryptionControl(BaseModel):
    State: StrictStr | None = None
    Mode: StrictStr | None = None
    Exclusions: EC2AccountVpcEncryptionControlExclusions | None = None
    ManagedBy: StrictStr | None = None
    LastUpdateTimestamp: datetime.datetime | StrictStr | None = None
