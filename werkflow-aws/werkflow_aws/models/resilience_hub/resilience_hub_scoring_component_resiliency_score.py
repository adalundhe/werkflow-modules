from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class ResilienceHubScoringComponentResiliencyScore(BaseModel):
    excludedCount: StrictInt | None = None
    outstandingCount: StrictInt | None = None
    possibleScore: StrictFloat | StrictInt | None = None
    score: StrictFloat | StrictInt | None = None
