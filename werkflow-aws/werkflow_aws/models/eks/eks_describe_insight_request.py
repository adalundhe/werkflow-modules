from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSDescribeInsightRequest(BaseModel):
    clusterName: StrictStr
    id: StrictStr
