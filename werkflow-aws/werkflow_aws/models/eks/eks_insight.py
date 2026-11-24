from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .eks_insight_category_specific_summary import EKSInsightCategorySpecificSummary
from .eks_insight_resource_detail import EKSInsightResourceDetail
from .eks_insight_status import EKSInsightStatus


class EKSInsight(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    category: StrictStr | None = None
    kubernetesVersion: StrictStr | None = None
    lastRefreshTime: datetime.datetime | StrictStr | None = None
    lastTransitionTime: datetime.datetime | StrictStr | None = None
    description: StrictStr | None = None
    insightStatus: EKSInsightStatus | None = None
    recommendation: StrictStr | None = None
    additionalInfo: dict[StrictStr, StrictStr] | None = None
    resources: list[EKSInsightResourceDetail] | None = None
    categorySpecificSummary: EKSInsightCategorySpecificSummary | None = None
