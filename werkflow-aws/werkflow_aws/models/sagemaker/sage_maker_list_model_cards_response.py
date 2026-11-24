from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_model_card_summary import SageMakerModelCardSummary


class SageMakerListModelCardsResponse(BaseModel):
    ModelCardSummaries: list[SageMakerModelCardSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
