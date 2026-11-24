from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_targeted_sentiment_entity import ComprehendTargetedSentimentEntity


class ComprehendDetectTargetedSentimentResponse(BaseModel):
    Entities: list[ComprehendTargetedSentimentEntity] | None = None
    ResponseMetadata: dict[str, Any] | None = None
