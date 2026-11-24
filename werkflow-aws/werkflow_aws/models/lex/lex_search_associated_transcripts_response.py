from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_associated_transcript import LexAssociatedTranscript


class LexSearchAssociatedTranscriptsResponse(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    botRecommendationId: StrictStr | None = None
    nextIndex: StrictInt | None = None
    associatedTranscripts: list[LexAssociatedTranscript] | None = None
    totalResults: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
