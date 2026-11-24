from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerReservationPurchaseRecommendationSummary(BaseModel):
    TotalEstimatedMonthlySavingsAmount: StrictStr | None = None
    TotalEstimatedMonthlySavingsPercentage: StrictStr | None = None
    CurrencyCode: StrictStr | None = None
