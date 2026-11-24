from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_static_ip import LightsailStaticIp


class LightsailGetStaticIpsResponse(BaseModel):
    staticIps: list[LightsailStaticIp] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
