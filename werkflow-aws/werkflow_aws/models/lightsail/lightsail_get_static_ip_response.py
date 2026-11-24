from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_static_ip import LightsailStaticIp


class LightsailGetStaticIpResponse(BaseModel):
    staticIp: LightsailStaticIp | None = None
    ResponseMetadata: dict[str, Any] | None = None
