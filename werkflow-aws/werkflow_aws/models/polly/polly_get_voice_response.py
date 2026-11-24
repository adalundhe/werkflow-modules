from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .polly_voice import PollyVoice


class PollyGetVoiceResponse(BaseModel):
    Voice: PollyVoice | None = None
    ResponseMetadata: dict[str, Any] | None = None
