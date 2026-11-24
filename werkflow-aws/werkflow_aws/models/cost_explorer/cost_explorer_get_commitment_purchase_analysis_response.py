from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cost_explorer_analysis_details import CostExplorerAnalysisDetails
from .cost_explorer_commitment_purchase_analysis_configuration import CostExplorerCommitmentPurchaseAnalysisConfiguration


class CostExplorerGetCommitmentPurchaseAnalysisResponse(BaseModel):
    EstimatedCompletionTime: StrictStr | None = None
    AnalysisCompletionTime: StrictStr | None = None
    AnalysisStartedTime: StrictStr | None = None
    AnalysisId: StrictStr | None = None
    AnalysisStatus: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    AnalysisDetails: CostExplorerAnalysisDetails | None = None
    CommitmentPurchaseAnalysisConfiguration: CostExplorerCommitmentPurchaseAnalysisConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
