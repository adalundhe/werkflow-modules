from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .transcribe_medical_transcription_job import TranscribeMedicalTranscriptionJob


class TranscribeGetMedicalTranscriptionJobResponse(BaseModel):
    MedicalTranscriptionJob: TranscribeMedicalTranscriptionJob | None = None
    ResponseMetadata: dict[str, Any] | None = None
