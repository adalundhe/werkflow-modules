from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transcribe_medical_scribe_job_summary import TranscribeMedicalScribeJobSummary


class TranscribeListMedicalScribeJobsResponse(BaseModel):
    Status: StrictStr | None = None
    NextToken: StrictStr | None = None
    MedicalScribeJobSummaries: list[TranscribeMedicalScribeJobSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
