from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_ebs_instance_block_device_specification import EC2EbsInstanceBlockDeviceSpecification


class EC2InstanceBlockDeviceMappingSpecification(BaseModel):
    DeviceName: StrictStr | None = None
    Ebs: EC2EbsInstanceBlockDeviceSpecification | None = None
    VirtualName: StrictStr | None = None
    NoDevice: StrictStr | None = None
