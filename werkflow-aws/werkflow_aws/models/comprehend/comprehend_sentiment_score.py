from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class ComprehendSentimentScore(BaseModel):
    Positive: StrictFloat | StrictInt | None = None
    Negative: StrictFloat | StrictInt | None = None
    Neutral: StrictFloat | StrictInt | None = None
    Mixed: StrictFloat | StrictInt | None = None
