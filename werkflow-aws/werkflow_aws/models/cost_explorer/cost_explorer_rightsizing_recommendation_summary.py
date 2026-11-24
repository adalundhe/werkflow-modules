from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerRightsizingRecommendationSummary(BaseModel):
    TotalRecommendationCount: StrictStr | None = None
    EstimatedTotalMonthlySavingsAmount: StrictStr | None = None
    SavingsCurrencyCode: StrictStr | None = None
    SavingsPercentage: StrictStr | None = None
