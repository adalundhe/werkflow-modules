from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CostExplorerRightsizingRecommendationConfiguration(BaseModel):
    RecommendationTarget: StrictStr | None = None
    BenefitsConsidered: StrictBool | None = None
