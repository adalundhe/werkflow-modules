from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_verify_otp_message_request_parameters import PinpointVerifyOTPMessageRequestParameters


class PinpointVerifyOTPMessageRequest(BaseModel):
    ApplicationId: StrictStr
    VerifyOTPMessageRequestParameters: PinpointVerifyOTPMessageRequestParameters
