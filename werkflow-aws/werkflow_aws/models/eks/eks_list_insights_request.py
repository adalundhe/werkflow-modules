from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .eks_insights_filter import EKSInsightsFilter


class EKSListInsightsRequest(BaseModel):
    clusterName: StrictStr
    filter: EKSInsightsFilter | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
