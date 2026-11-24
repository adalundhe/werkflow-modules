from __future__ import annotations
from pydantic import BaseModel
from .ecr_recommendation import ECRRecommendation


class ECRRemediation(BaseModel):
    recommendation: ECRRecommendation | None = None
