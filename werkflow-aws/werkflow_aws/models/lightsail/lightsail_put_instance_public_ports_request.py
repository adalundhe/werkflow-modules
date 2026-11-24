from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_port_info import LightsailPortInfo


class LightsailPutInstancePublicPortsRequest(BaseModel):
    portInfos: list[LightsailPortInfo]
    instanceName: StrictStr
