from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_message_body import PinpointMessageBody


class PinpointDeleteVoiceTemplateResponse(BaseModel):
    MessageBody: PinpointMessageBody | None = None
    ResponseMetadata: dict[str, Any] | None = None
