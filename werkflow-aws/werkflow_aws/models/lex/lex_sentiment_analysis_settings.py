from __future__ import annotations
from pydantic import BaseModel, StrictBool


class LexSentimentAnalysisSettings(BaseModel):
    detectSentiment: StrictBool | None = None
