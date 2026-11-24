from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_savings_plans_details import CostExplorerSavingsPlansDetails


class CostExplorerSavingsPlansPurchaseRecommendationDetail(BaseModel):
    SavingsPlansDetails: CostExplorerSavingsPlansDetails | None = None
    AccountId: StrictStr | None = None
    UpfrontCost: StrictStr | None = None
    EstimatedROI: StrictStr | None = None
    CurrencyCode: StrictStr | None = None
    EstimatedSPCost: StrictStr | None = None
    EstimatedOnDemandCost: StrictStr | None = None
    EstimatedOnDemandCostWithCurrentCommitment: StrictStr | None = None
    EstimatedSavingsAmount: StrictStr | None = None
    EstimatedSavingsPercentage: StrictStr | None = None
    HourlyCommitmentToPurchase: StrictStr | None = None
    EstimatedAverageUtilization: StrictStr | None = None
    EstimatedMonthlySavingsAmount: StrictStr | None = None
    CurrentMinimumHourlyOnDemandSpend: StrictStr | None = None
    CurrentMaximumHourlyOnDemandSpend: StrictStr | None = None
    CurrentAverageHourlyOnDemandSpend: StrictStr | None = None
    RecommendationDetailId: StrictStr | None = None
