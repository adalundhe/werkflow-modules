from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2TrafficMirrorSession(BaseModel):
    TrafficMirrorSessionId: StrictStr | None = None
    TrafficMirrorTargetId: StrictStr | None = None
    TrafficMirrorFilterId: StrictStr | None = None
    NetworkInterfaceId: StrictStr | None = None
    OwnerId: StrictStr | None = None
    PacketLength: StrictInt | None = None
    SessionNumber: StrictInt | None = None
    VirtualNetworkId: StrictInt | None = None
    Description: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
