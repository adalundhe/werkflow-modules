from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class LexStopBotRecommendationResponse(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    botRecommendationStatus: StrictStr | None = None
    botRecommendationId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
