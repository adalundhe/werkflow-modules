from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_sms_channel_request import PinpointSMSChannelRequest


class PinpointUpdateSmsChannelRequest(BaseModel):
    ApplicationId: StrictStr
    SMSChannelRequest: PinpointSMSChannelRequest
