from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeDeleteMedicalScribeJobRequest(BaseModel):
    MedicalScribeJobName: StrictStr
