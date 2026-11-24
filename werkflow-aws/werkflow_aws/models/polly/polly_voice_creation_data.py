from __future__ import annotations
from pydantic import BaseModel
from .polly_recording import PollyRecording


class PollyVoiceCreationData(BaseModel):
    Recordings: list[PollyRecording] | None = None
