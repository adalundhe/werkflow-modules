from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cost_explorer_reservation_purchase_recommendation import CostExplorerReservationPurchaseRecommendation
from .cost_explorer_reservation_purchase_recommendation_metadata import CostExplorerReservationPurchaseRecommendationMetadata


class CostExplorerGetReservationPurchaseRecommendationResponse(BaseModel):
    Metadata: CostExplorerReservationPurchaseRecommendationMetadata | None = None
    Recommendations: list[CostExplorerReservationPurchaseRecommendation] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
