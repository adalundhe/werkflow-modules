from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_in_app_messages_response import PinpointInAppMessagesResponse


class PinpointGetInAppMessagesResponse(BaseModel):
    InAppMessagesResponse: PinpointInAppMessagesResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
