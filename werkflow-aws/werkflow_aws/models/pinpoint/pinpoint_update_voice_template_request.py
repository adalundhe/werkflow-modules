from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .pinpoint_voice_template_request import PinpointVoiceTemplateRequest


class PinpointUpdateVoiceTemplateRequest(BaseModel):
    TemplateName: StrictStr
    VoiceTemplateRequest: PinpointVoiceTemplateRequest
    CreateNewVersion: StrictBool | None = None
    Version: StrictStr | None = None
