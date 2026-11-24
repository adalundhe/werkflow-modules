from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dms_recommendation_settings import DMSRecommendationSettings


class DMSStartRecommendationsRequestEntry(BaseModel):
    DatabaseId: StrictStr
    Settings: DMSRecommendationSettings
