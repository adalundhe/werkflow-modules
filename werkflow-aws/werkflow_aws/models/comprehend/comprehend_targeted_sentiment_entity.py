from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .comprehend_targeted_sentiment_mention import ComprehendTargetedSentimentMention


class ComprehendTargetedSentimentEntity(BaseModel):
    DescriptiveMentionIndex: list[StrictInt] | None = None
    Mentions: list[ComprehendTargetedSentimentMention] | None = None
