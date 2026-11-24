from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComputeOptimizerGetEffectiveRecommendationPreferencesRequest(BaseModel):
    resourceArn: StrictStr
