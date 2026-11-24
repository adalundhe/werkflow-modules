from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_voice_template_response import PinpointVoiceTemplateResponse


class PinpointGetVoiceTemplateResponse(BaseModel):
    VoiceTemplateResponse: PinpointVoiceTemplateResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
