from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LexSlotResolutionTestResultItemCounts(BaseModel):
    totalResultCount: StrictInt | None = None
    speechTranscriptionResultCounts: dict[StrictStr, StrictInt] | None = None
    slotMatchResultCounts: dict[StrictStr, StrictInt] | None = None
