from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexDescribeBotRecommendationRequest(BaseModel):
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
    botRecommendationId: StrictStr
