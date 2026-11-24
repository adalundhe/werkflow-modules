from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_search_record import SageMakerSearchRecord
from .sage_maker_total_hits import SageMakerTotalHits


class SageMakerSearchResponse(BaseModel):
    Results: list[SageMakerSearchRecord] | None = None
    NextToken: StrictStr | None = None
    TotalHits: SageMakerTotalHits | None = None
    ResponseMetadata: dict[str, Any] | None = None
