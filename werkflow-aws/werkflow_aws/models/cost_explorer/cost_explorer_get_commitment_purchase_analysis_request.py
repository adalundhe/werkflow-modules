from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerGetCommitmentPurchaseAnalysisRequest(BaseModel):
    AnalysisId: StrictStr
