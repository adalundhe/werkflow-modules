from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class LexOverallTestResultItem(BaseModel):
    multiTurnConversation: StrictBool | None = None
    totalResultCount: StrictInt | None = None
    speechTranscriptionResultCounts: dict[StrictStr, StrictInt] | None = None
    endToEndResultCounts: dict[StrictStr, StrictInt] | None = None
