from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeGetTranscriptionJobRequest(BaseModel):
    TranscriptionJobName: StrictStr
