from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_savings_plans_purchase_recommendation_detail import CostExplorerSavingsPlansPurchaseRecommendationDetail
from .cost_explorer_savings_plans_purchase_recommendation_summary import CostExplorerSavingsPlansPurchaseRecommendationSummary


class CostExplorerSavingsPlansPurchaseRecommendation(BaseModel):
    AccountScope: StrictStr | None = None
    SavingsPlansType: StrictStr | None = None
    TermInYears: StrictStr | None = None
    PaymentOption: StrictStr | None = None
    LookbackPeriodInDays: StrictStr | None = None
    SavingsPlansPurchaseRecommendationDetails: list[CostExplorerSavingsPlansPurchaseRecommendationDetail] | None = None
    SavingsPlansPurchaseRecommendationSummary: CostExplorerSavingsPlansPurchaseRecommendationSummary | None = None
