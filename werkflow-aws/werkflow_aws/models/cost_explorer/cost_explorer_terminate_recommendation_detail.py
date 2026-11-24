from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerTerminateRecommendationDetail(BaseModel):
    EstimatedMonthlySavings: StrictStr | None = None
    CurrencyCode: StrictStr | None = None
