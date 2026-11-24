from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeMedicalTranscript(BaseModel):
    TranscriptFileUri: StrictStr | None = None
