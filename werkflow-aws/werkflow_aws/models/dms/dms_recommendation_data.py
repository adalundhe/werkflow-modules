from __future__ import annotations
from pydantic import BaseModel
from .dms_rds_recommendation import DMSRdsRecommendation


class DMSRecommendationData(BaseModel):
    RdsEngine: DMSRdsRecommendation | None = None
