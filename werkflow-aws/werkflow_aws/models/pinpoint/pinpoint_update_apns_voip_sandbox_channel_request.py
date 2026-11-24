from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_apns_voip_sandbox_channel_request import PinpointAPNSVoipSandboxChannelRequest


class PinpointUpdateApnsVoipSandboxChannelRequest(BaseModel):
    APNSVoipSandboxChannelRequest: PinpointAPNSVoipSandboxChannelRequest
    ApplicationId: StrictStr
