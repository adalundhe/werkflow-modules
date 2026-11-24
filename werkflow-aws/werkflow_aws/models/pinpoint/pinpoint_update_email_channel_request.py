from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_email_channel_request import PinpointEmailChannelRequest


class PinpointUpdateEmailChannelRequest(BaseModel):
    ApplicationId: StrictStr
    EmailChannelRequest: PinpointEmailChannelRequest
