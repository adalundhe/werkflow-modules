from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .polly_start_speech_synthesis_stream_event_stream import PollyStartSpeechSynthesisStreamEventStream


class PollyStartSpeechSynthesisStreamResponse(BaseModel):
    EventStream: PollyStartSpeechSynthesisStreamEventStream | None = None
    ResponseMetadata: dict[str, Any] | None = None
