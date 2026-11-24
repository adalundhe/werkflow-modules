from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_apns_sandbox_channel_request import PinpointAPNSSandboxChannelRequest


class PinpointUpdateApnsSandboxChannelRequest(BaseModel):
    APNSSandboxChannelRequest: PinpointAPNSSandboxChannelRequest
    ApplicationId: StrictStr
