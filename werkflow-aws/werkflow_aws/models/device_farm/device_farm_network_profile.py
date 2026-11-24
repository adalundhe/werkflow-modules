from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DeviceFarmNetworkProfile(BaseModel):
    arn: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    type: StrictStr | None = None
    uplinkBandwidthBits: StrictInt | None = None
    downlinkBandwidthBits: StrictInt | None = None
    uplinkDelayMs: StrictInt | None = None
    downlinkDelayMs: StrictInt | None = None
    uplinkJitterMs: StrictInt | None = None
    downlinkJitterMs: StrictInt | None = None
    uplinkLossPercent: StrictInt | None = None
    downlinkLossPercent: StrictInt | None = None
