from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_launch_template_ebs_block_device import EC2LaunchTemplateEbsBlockDevice


class EC2LaunchTemplateBlockDeviceMapping(BaseModel):
    DeviceName: StrictStr | None = None
    VirtualName: StrictStr | None = None
    Ebs: EC2LaunchTemplateEbsBlockDevice | None = None
    NoDevice: StrictStr | None = None
