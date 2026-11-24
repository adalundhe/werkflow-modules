from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_voice_template_request import PinpointVoiceTemplateRequest


class PinpointCreateVoiceTemplateRequest(BaseModel):
    TemplateName: StrictStr
    VoiceTemplateRequest: PinpointVoiceTemplateRequest
