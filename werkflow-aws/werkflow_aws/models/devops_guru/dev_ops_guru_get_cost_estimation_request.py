from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DevOpsGuruGetCostEstimationRequest(BaseModel):
    NextToken: StrictStr | None = None
