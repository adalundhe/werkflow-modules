from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_send_otp_message_request_parameters import PinpointSendOTPMessageRequestParameters


class PinpointSendOTPMessageRequest(BaseModel):
    ApplicationId: StrictStr
    SendOTPMessageRequestParameters: PinpointSendOTPMessageRequestParameters
