from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DeviceFarmCreateNetworkProfileRequest(BaseModel):
    projectArn: StrictStr
    name: StrictStr
    description: StrictStr | None = None
    type: Literal['CURATED', 'PRIVATE'] | None = None
    uplinkBandwidthBits: StrictInt | None = None
    downlinkBandwidthBits: StrictInt | None = None
    uplinkDelayMs: StrictInt | None = None
    downlinkDelayMs: StrictInt | None = None
    uplinkJitterMs: StrictInt | None = None
    downlinkJitterMs: StrictInt | None = None
    uplinkLossPercent: StrictInt | None = None
    downlinkLossPercent: StrictInt | None = None
