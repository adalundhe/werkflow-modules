from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transcribe_medical_transcription_job_summary import TranscribeMedicalTranscriptionJobSummary


class TranscribeListMedicalTranscriptionJobsResponse(BaseModel):
    Status: StrictStr | None = None
    NextToken: StrictStr | None = None
    MedicalTranscriptionJobSummaries: list[TranscribeMedicalTranscriptionJobSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
