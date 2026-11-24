from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointVerifyOTPMessageRequestParameters(BaseModel):
    DestinationIdentity: StrictStr
    Otp: StrictStr
    ReferenceId: StrictStr
