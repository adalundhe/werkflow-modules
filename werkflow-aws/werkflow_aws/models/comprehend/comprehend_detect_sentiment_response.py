from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .comprehend_sentiment_score import ComprehendSentimentScore


class ComprehendDetectSentimentResponse(BaseModel):
    Sentiment: StrictStr | None = None
    SentimentScore: ComprehendSentimentScore | None = None
    ResponseMetadata: dict[str, Any] | None = None
