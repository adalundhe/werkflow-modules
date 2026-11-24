from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_create_template_message_body import PinpointCreateTemplateMessageBody


class PinpointCreateVoiceTemplateResponse(BaseModel):
    CreateTemplateMessageBody: PinpointCreateTemplateMessageBody | None = None
    ResponseMetadata: dict[str, Any] | None = None
