from __future__ import annotations
from pydantic import BaseModel
from .polly_close_stream_event import PollyCloseStreamEvent
from .polly_text_event import PollyTextEvent


class PollyStartSpeechSynthesisStreamActionStream(BaseModel):
    TextEvent: PollyTextEvent | None = None
    CloseStreamEvent: PollyCloseStreamEvent | None = None
