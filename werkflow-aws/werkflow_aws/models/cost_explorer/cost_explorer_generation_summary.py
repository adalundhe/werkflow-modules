from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerGenerationSummary(BaseModel):
    RecommendationId: StrictStr | None = None
    GenerationStatus: StrictStr | None = None
    GenerationStartedTime: StrictStr | None = None
    GenerationCompletionTime: StrictStr | None = None
    EstimatedCompletionTime: StrictStr | None = None
