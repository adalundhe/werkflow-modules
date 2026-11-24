from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transcribe_transcription_job_summary import TranscribeTranscriptionJobSummary


class TranscribeListTranscriptionJobsResponse(BaseModel):
    Status: StrictStr | None = None
    NextToken: StrictStr | None = None
    TranscriptionJobSummaries: list[TranscribeTranscriptionJobSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
