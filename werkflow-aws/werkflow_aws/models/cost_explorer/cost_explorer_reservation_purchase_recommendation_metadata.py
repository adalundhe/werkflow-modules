from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerReservationPurchaseRecommendationMetadata(BaseModel):
    RecommendationId: StrictStr | None = None
    GenerationTimestamp: StrictStr | None = None
    AdditionalMetadata: StrictStr | None = None
