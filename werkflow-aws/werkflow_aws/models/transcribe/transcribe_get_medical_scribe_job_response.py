from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .transcribe_medical_scribe_job import TranscribeMedicalScribeJob


class TranscribeGetMedicalScribeJobResponse(BaseModel):
    MedicalScribeJob: TranscribeMedicalScribeJob | None = None
    ResponseMetadata: dict[str, Any] | None = None
