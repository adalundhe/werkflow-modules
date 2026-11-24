from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LexIntentClassificationTestResultItemCounts(BaseModel):
    totalResultCount: StrictInt | None = None
    speechTranscriptionResultCounts: dict[StrictStr, StrictInt] | None = None
    intentMatchResultCounts: dict[StrictStr, StrictInt] | None = None
