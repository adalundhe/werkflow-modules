from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeMedicalScribeOutput(BaseModel):
    TranscriptFileUri: StrictStr | None = None
    ClinicalDocumentUri: StrictStr | None = None
