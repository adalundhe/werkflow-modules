from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .comprehend_sentiment_score import ComprehendSentimentScore


class ComprehendMentionSentiment(BaseModel):
    Sentiment: StrictStr | None = None
    SentimentScore: ComprehendSentimentScore | None = None
