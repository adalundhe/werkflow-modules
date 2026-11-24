from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_port_info import LightsailPortInfo


class LightsailOpenInstancePublicPortsRequest(BaseModel):
    portInfo: LightsailPortInfo
    instanceName: StrictStr
