from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_bot_recommendation_summary import LexBotRecommendationSummary


class LexListBotRecommendationsResponse(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    botRecommendationSummaries: list[LexBotRecommendationSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
