from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_sms_channel_response import PinpointSMSChannelResponse


class PinpointGetSmsChannelResponse(BaseModel):
    SMSChannelResponse: PinpointSMSChannelResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
