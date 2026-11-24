from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_verification_response import PinpointVerificationResponse


class PinpointVerifyOTPMessageResponse(BaseModel):
    VerificationResponse: PinpointVerificationResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
