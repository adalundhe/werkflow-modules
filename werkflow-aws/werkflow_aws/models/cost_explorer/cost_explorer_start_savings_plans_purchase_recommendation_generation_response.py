from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CostExplorerStartSavingsPlansPurchaseRecommendationGenerationResponse(BaseModel):
    RecommendationId: StrictStr | None = None
    GenerationStartedTime: StrictStr | None = None
    EstimatedCompletionTime: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
