from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cost_explorer_generation_summary import CostExplorerGenerationSummary


class CostExplorerListSavingsPlansPurchaseRecommendationGenerationResponse(BaseModel):
    GenerationSummaryList: list[CostExplorerGenerationSummary] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
