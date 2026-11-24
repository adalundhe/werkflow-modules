from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_associated_transcript_filter import LexAssociatedTranscriptFilter


class LexSearchAssociatedTranscriptsRequest(BaseModel):
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
    botRecommendationId: StrictStr
    filters: list[LexAssociatedTranscriptFilter]
    searchOrder: Literal['Ascending', 'Descending'] | None = None
    maxResults: StrictInt | None = None
    nextIndex: StrictInt | None = None
