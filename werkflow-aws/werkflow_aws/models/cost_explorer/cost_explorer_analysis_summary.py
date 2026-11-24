from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_commitment_purchase_analysis_configuration import CostExplorerCommitmentPurchaseAnalysisConfiguration


class CostExplorerAnalysisSummary(BaseModel):
    EstimatedCompletionTime: StrictStr | None = None
    AnalysisCompletionTime: StrictStr | None = None
    AnalysisStartedTime: StrictStr | None = None
    AnalysisStatus: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    AnalysisId: StrictStr | None = None
    CommitmentPurchaseAnalysisConfiguration: CostExplorerCommitmentPurchaseAnalysisConfiguration | None = None
