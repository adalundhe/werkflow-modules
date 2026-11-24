from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_recommendation_related_anomaly_resource import DevOpsGuruRecommendationRelatedAnomalyResource
from .dev_ops_guru_recommendation_related_anomaly_source_detail import DevOpsGuruRecommendationRelatedAnomalySourceDetail


class DevOpsGuruRecommendationRelatedAnomaly(BaseModel):
    Resources: list[DevOpsGuruRecommendationRelatedAnomalyResource] | None = None
    SourceDetails: list[DevOpsGuruRecommendationRelatedAnomalySourceDetail] | None = None
    AnomalyId: StrictStr | None = None
