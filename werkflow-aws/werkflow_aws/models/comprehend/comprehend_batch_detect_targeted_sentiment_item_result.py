from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .comprehend_targeted_sentiment_entity import ComprehendTargetedSentimentEntity


class ComprehendBatchDetectTargetedSentimentItemResult(BaseModel):
    Index: StrictInt | None = None
    Entities: list[ComprehendTargetedSentimentEntity] | None = None
