from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_recommendation_related_anomaly import DevOpsGuruRecommendationRelatedAnomaly
from .dev_ops_guru_recommendation_related_event import DevOpsGuruRecommendationRelatedEvent


class DevOpsGuruRecommendation(BaseModel):
    Description: StrictStr | None = None
    Link: StrictStr | None = None
    Name: StrictStr | None = None
    Reason: StrictStr | None = None
    RelatedEvents: list[DevOpsGuruRecommendationRelatedEvent] | None = None
    RelatedAnomalies: list[DevOpsGuruRecommendationRelatedAnomaly] | None = None
    Category: StrictStr | None = None
