from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .comprehend_sentiment_score import ComprehendSentimentScore


class ComprehendBatchDetectSentimentItemResult(BaseModel):
    Index: StrictInt | None = None
    Sentiment: StrictStr | None = None
    SentimentScore: ComprehendSentimentScore | None = None
