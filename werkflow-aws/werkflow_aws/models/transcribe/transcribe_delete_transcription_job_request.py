from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeDeleteTranscriptionJobRequest(BaseModel):
    TranscriptionJobName: StrictStr
