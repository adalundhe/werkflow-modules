from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CostExplorerStartCommitmentPurchaseAnalysisResponse(BaseModel):
    AnalysisId: StrictStr | None = None
    AnalysisStartedTime: StrictStr | None = None
    EstimatedCompletionTime: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
