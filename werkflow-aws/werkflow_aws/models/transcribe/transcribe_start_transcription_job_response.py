from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .transcribe_transcription_job import TranscribeTranscriptionJob


class TranscribeStartTranscriptionJobResponse(BaseModel):
    TranscriptionJob: TranscribeTranscriptionJob | None = None
    ResponseMetadata: dict[str, Any] | None = None
