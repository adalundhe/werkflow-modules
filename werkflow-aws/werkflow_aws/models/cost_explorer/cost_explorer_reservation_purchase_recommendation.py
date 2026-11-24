from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_reservation_purchase_recommendation_detail import CostExplorerReservationPurchaseRecommendationDetail
from .cost_explorer_reservation_purchase_recommendation_summary import CostExplorerReservationPurchaseRecommendationSummary
from .cost_explorer_service_specification import CostExplorerServiceSpecification


class CostExplorerReservationPurchaseRecommendation(BaseModel):
    AccountScope: StrictStr | None = None
    LookbackPeriodInDays: StrictStr | None = None
    TermInYears: StrictStr | None = None
    PaymentOption: StrictStr | None = None
    ServiceSpecification: CostExplorerServiceSpecification | None = None
    RecommendationDetails: list[CostExplorerReservationPurchaseRecommendationDetail] | None = None
    RecommendationSummary: CostExplorerReservationPurchaseRecommendationSummary | None = None
