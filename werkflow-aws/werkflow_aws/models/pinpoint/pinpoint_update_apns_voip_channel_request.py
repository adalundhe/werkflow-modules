from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_apns_voip_channel_request import PinpointAPNSVoipChannelRequest


class PinpointUpdateApnsVoipChannelRequest(BaseModel):
    APNSVoipChannelRequest: PinpointAPNSVoipChannelRequest
    ApplicationId: StrictStr
