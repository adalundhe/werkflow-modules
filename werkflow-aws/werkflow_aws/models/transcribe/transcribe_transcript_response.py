from __future__ import annotations
from pydantic import BaseModel
from .transcribe_audio_metadata import TranscribeAudioMetadata
from .transcribe_audio_results import TranscribeAudioResults


class TranscribeTranscriptResponse(BaseModel):
    Metadata: TranscribeAudioMetadata | None = None
    Results: TranscribeAudioResults | None = None
    RedactedResults: TranscribeAudioResults | None = None
