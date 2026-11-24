from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dms_recommendation_settings import DMSRecommendationSettings


class DMSStartRecommendationsRequest(BaseModel):
    DatabaseId: StrictStr
    Settings: DMSRecommendationSettings
