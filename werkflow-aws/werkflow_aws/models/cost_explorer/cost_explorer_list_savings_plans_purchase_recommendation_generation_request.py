from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CostExplorerListSavingsPlansPurchaseRecommendationGenerationRequest(BaseModel):
    GenerationStatus: Literal['SUCCEEDED', 'PROCESSING', 'FAILED'] | None = None
    RecommendationIds: list[StrictStr] | None = None
    PageSize: StrictInt | None = None
    NextPageToken: StrictStr | None = None
