from __future__ import annotations
from pydantic import BaseModel
from .connect_transcript import ConnectTranscript


class ConnectContactAnalysis(BaseModel):
    Transcript: ConnectTranscript | None = None
