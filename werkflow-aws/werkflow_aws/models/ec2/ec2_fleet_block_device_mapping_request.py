from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_fleet_ebs_block_device_request import EC2FleetEbsBlockDeviceRequest


class EC2FleetBlockDeviceMappingRequest(BaseModel):
    DeviceName: StrictStr | None = None
    VirtualName: StrictStr | None = None
    Ebs: EC2FleetEbsBlockDeviceRequest | None = None
    NoDevice: StrictStr | None = None
