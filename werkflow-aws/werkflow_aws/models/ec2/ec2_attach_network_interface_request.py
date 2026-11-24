from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_ena_srd_specification import EC2EnaSrdSpecification


class EC2AttachNetworkInterfaceRequest(BaseModel):
    NetworkInterfaceId: StrictStr
    InstanceId: StrictStr
    DeviceIndex: StrictInt
    NetworkCardIndex: StrictInt | None = None
    EnaSrdSpecification: EC2EnaSrdSpecification | None = None
    EnaQueueCount: StrictInt | None = None
    DryRun: StrictBool | None = None
