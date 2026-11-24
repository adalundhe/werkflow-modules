from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_message_response import PinpointMessageResponse


class PinpointSendOTPMessageResponse(BaseModel):
    MessageResponse: PinpointMessageResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
