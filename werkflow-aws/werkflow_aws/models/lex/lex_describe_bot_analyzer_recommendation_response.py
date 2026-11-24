from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_bot_analyzer_recommendation import LexBotAnalyzerRecommendation


class LexDescribeBotAnalyzerRecommendationResponse(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    botAnalyzerStatus: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    botAnalyzerRecommendationList: list[LexBotAnalyzerRecommendation] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
