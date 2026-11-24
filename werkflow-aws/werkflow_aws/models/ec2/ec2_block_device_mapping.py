from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_ebs_block_device import EC2EbsBlockDevice


class EC2BlockDeviceMapping(BaseModel):
    Ebs: EC2EbsBlockDevice | None = None
    NoDevice: StrictStr | None = None
    DeviceName: StrictStr | None = None
    VirtualName: StrictStr | None = None
