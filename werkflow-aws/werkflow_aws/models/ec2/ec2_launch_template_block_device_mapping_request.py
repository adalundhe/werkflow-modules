from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_launch_template_ebs_block_device_request import EC2LaunchTemplateEbsBlockDeviceRequest


class EC2LaunchTemplateBlockDeviceMappingRequest(BaseModel):
    DeviceName: StrictStr | None = None
    VirtualName: StrictStr | None = None
    Ebs: EC2LaunchTemplateEbsBlockDeviceRequest | None = None
    NoDevice: StrictStr | None = None
