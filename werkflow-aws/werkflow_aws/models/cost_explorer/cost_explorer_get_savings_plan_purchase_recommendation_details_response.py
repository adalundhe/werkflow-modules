from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cost_explorer_recommendation_detail_data import CostExplorerRecommendationDetailData


class CostExplorerGetSavingsPlanPurchaseRecommendationDetailsResponse(BaseModel):
    RecommendationDetailId: StrictStr | None = None
    RecommendationDetailData: CostExplorerRecommendationDetailData | None = None
    ResponseMetadata: dict[str, Any] | None = None
