from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CostExplorerListCommitmentPurchaseAnalysesRequest(BaseModel):
    AnalysisStatus: Literal['SUCCEEDED', 'PROCESSING', 'FAILED'] | None = None
    NextPageToken: StrictStr | None = None
    PageSize: StrictInt | None = None
    AnalysisIds: list[StrictStr] | None = None
