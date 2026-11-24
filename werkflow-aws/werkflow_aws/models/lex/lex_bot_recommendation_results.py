from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_bot_recommendation_result_statistics import LexBotRecommendationResultStatistics


class LexBotRecommendationResults(BaseModel):
    botLocaleExportUrl: StrictStr | None = None
    associatedTranscriptsUrl: StrictStr | None = None
    statistics: LexBotRecommendationResultStatistics | None = None
