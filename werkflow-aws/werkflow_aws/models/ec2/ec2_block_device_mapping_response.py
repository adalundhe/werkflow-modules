from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_ebs_block_device_response import EC2EbsBlockDeviceResponse


class EC2BlockDeviceMappingResponse(BaseModel):
    DeviceName: StrictStr | None = None
    VirtualName: StrictStr | None = None
    Ebs: EC2EbsBlockDeviceResponse | None = None
    NoDevice: StrictStr | None = None
