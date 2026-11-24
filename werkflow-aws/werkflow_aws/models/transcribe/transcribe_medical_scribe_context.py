from __future__ import annotations
from pydantic import BaseModel
from .transcribe_medical_scribe_patient_context import TranscribeMedicalScribePatientContext


class TranscribeMedicalScribeContext(BaseModel):
    PatientContext: TranscribeMedicalScribePatientContext | None = None
