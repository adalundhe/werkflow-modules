from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_recommended_intent_summary import LexRecommendedIntentSummary


class LexListRecommendedIntentsResponse(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    botRecommendationId: StrictStr | None = None
    summaryList: list[LexRecommendedIntentSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
