from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .eks_insight_status import EKSInsightStatus


class EKSInsightSummary(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    category: StrictStr | None = None
    kubernetesVersion: StrictStr | None = None
    lastRefreshTime: datetime.datetime | StrictStr | None = None
    lastTransitionTime: datetime.datetime | StrictStr | None = None
    description: StrictStr | None = None
    insightStatus: EKSInsightStatus | None = None
