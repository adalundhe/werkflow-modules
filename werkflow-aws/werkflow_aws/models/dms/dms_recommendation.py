from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .dms_recommendation_data import DMSRecommendationData
from .dms_recommendation_settings import DMSRecommendationSettings


class DMSRecommendation(BaseModel):
    DatabaseId: StrictStr | None = None
    EngineName: StrictStr | None = None
    CreatedDate: StrictStr | None = None
    Status: StrictStr | None = None
    Preferred: StrictBool | None = None
    Settings: DMSRecommendationSettings | None = None
    Data: DMSRecommendationData | None = None
