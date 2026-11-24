from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_recommendation_related_event_resource import DevOpsGuruRecommendationRelatedEventResource


class DevOpsGuruRecommendationRelatedEvent(BaseModel):
    Name: StrictStr | None = None
    Resources: list[DevOpsGuruRecommendationRelatedEventResource] | None = None
