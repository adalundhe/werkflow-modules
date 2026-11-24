from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cost_explorer_savings_plans_purchase_recommendation import CostExplorerSavingsPlansPurchaseRecommendation
from .cost_explorer_savings_plans_purchase_recommendation_metadata import CostExplorerSavingsPlansPurchaseRecommendationMetadata


class CostExplorerGetSavingsPlansPurchaseRecommendationResponse(BaseModel):
    Metadata: CostExplorerSavingsPlansPurchaseRecommendationMetadata | None = None
    SavingsPlansPurchaseRecommendation: CostExplorerSavingsPlansPurchaseRecommendation | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
