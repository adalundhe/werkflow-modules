from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_gcm_channel_request import PinpointGCMChannelRequest


class PinpointUpdateGcmChannelRequest(BaseModel):
    ApplicationId: StrictStr
    GCMChannelRequest: PinpointGCMChannelRequest
