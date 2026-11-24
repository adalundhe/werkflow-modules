from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_recommended_action_update import RDSRecommendedActionUpdate


class RDSModifyDBRecommendationRequest(BaseModel):
    RecommendationId: StrictStr
    Locale: StrictStr | None = None
    Status: StrictStr | None = None
    RecommendedActionUpdates: list[RDSRecommendedActionUpdate] | None = None
