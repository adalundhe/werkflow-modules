from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_apns_channel_request import PinpointAPNSChannelRequest


class PinpointUpdateApnsChannelRequest(BaseModel):
    APNSChannelRequest: PinpointAPNSChannelRequest
    ApplicationId: StrictStr
