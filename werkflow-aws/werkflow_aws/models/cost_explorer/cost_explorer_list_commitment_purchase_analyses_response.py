from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cost_explorer_analysis_summary import CostExplorerAnalysisSummary


class CostExplorerListCommitmentPurchaseAnalysesResponse(BaseModel):
    AnalysisSummaryList: list[CostExplorerAnalysisSummary] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
