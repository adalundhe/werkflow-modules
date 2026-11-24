from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerSavingsPlansPurchaseRecommendationSummary(BaseModel):
    EstimatedROI: StrictStr | None = None
    CurrencyCode: StrictStr | None = None
    EstimatedTotalCost: StrictStr | None = None
    CurrentOnDemandSpend: StrictStr | None = None
    EstimatedSavingsAmount: StrictStr | None = None
    TotalRecommendationCount: StrictStr | None = None
    DailyCommitmentToPurchase: StrictStr | None = None
    HourlyCommitmentToPurchase: StrictStr | None = None
    EstimatedSavingsPercentage: StrictStr | None = None
    EstimatedMonthlySavingsAmount: StrictStr | None = None
    EstimatedOnDemandCostWithCurrentCommitment: StrictStr | None = None
