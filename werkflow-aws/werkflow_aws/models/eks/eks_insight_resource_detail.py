from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_insight_status import EKSInsightStatus


class EKSInsightResourceDetail(BaseModel):
    insightStatus: EKSInsightStatus | None = None
    kubernetesResourceUri: StrictStr | None = None
    arn: StrictStr | None = None
