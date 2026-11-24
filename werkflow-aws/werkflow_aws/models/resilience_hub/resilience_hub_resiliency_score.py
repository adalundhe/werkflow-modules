from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .resilience_hub_scoring_component_resiliency_score import ResilienceHubScoringComponentResiliencyScore


class ResilienceHubResiliencyScore(BaseModel):
    componentScore: dict[StrictStr, ResilienceHubScoringComponentResiliencyScore] | None = None
    disruptionScore: dict[StrictStr, StrictFloat | StrictInt] | None = None
    score: StrictFloat | StrictInt | None = None
