from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_recommendation import SESRecommendation


class SESListRecommendationsResponse(BaseModel):
    Recommendations: list[SESRecommendation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
