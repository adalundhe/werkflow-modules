from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_ebs_instance_block_device import EC2EbsInstanceBlockDevice


class EC2InstanceBlockDeviceMapping(BaseModel):
    DeviceName: StrictStr | None = None
    Ebs: EC2EbsInstanceBlockDevice | None = None
