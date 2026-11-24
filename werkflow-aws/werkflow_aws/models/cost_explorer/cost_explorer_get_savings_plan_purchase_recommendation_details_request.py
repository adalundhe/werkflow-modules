from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerGetSavingsPlanPurchaseRecommendationDetailsRequest(BaseModel):
    RecommendationDetailId: StrictStr
