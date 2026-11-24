from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateTrafficMirrorSessionRequest(BaseModel):
    NetworkInterfaceId: StrictStr
    TrafficMirrorTargetId: StrictStr
    TrafficMirrorFilterId: StrictStr
    SessionNumber: StrictInt
    PacketLength: StrictInt | None = None
    VirtualNetworkId: StrictInt | None = None
    Description: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    DryRun: StrictBool | None = None
    ClientToken: StrictStr | None = None
