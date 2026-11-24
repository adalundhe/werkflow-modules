from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .transcribe_sync_output_configuration import TranscribeSyncOutputConfiguration
from .transcribe_transcript_response import TranscribeTranscriptResponse


class TranscribeTranscribeAudioResponse(BaseModel):
    OutputConfiguration: TranscribeSyncOutputConfiguration | None = None
    TranscriptResponse: TranscribeTranscriptResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
