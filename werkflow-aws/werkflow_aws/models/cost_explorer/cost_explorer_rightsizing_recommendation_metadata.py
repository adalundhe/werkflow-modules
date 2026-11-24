from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerRightsizingRecommendationMetadata(BaseModel):
    RecommendationId: StrictStr | None = None
    GenerationTimestamp: StrictStr | None = None
    LookbackPeriodInDays: StrictStr | None = None
    AdditionalMetadata: StrictStr | None = None
