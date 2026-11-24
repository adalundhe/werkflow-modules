from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexDeleteBotAnalyzerRecommendationRequest(BaseModel):
    botId: StrictStr
    botAnalyzerRequestId: StrictStr
