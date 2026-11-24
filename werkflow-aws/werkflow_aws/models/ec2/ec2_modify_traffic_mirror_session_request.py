from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2ModifyTrafficMirrorSessionRequest(BaseModel):
    TrafficMirrorSessionId: StrictStr
    TrafficMirrorTargetId: StrictStr | None = None
    TrafficMirrorFilterId: StrictStr | None = None
    PacketLength: StrictInt | None = None
    SessionNumber: StrictInt | None = None
    VirtualNetworkId: StrictInt | None = None
    Description: StrictStr | None = None
    RemoveFields: list[Literal['packet-length', 'description', 'virtual-network-id']] | None = None
    DryRun: StrictBool | None = None
