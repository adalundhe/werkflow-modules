from __future__ import annotations
from pydantic import BaseModel, StrictBool


class TranscribeSummarization(BaseModel):
    GenerateAbstractiveSummary: StrictBool | None = None
