from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeDeleteMedicalTranscriptionJobRequest(BaseModel):
    MedicalTranscriptionJobName: StrictStr
