from __future__ import annotations
from pydantic import BaseModel
from .pinpoint_template import PinpointTemplate


class PinpointTemplateConfiguration(BaseModel):
    EmailTemplate: PinpointTemplate | None = None
    PushTemplate: PinpointTemplate | None = None
    SMSTemplate: PinpointTemplate | None = None
    VoiceTemplate: PinpointTemplate | None = None
    InAppTemplate: PinpointTemplate | None = None
