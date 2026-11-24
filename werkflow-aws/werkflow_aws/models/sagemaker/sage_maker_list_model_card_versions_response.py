from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_model_card_version_summary import SageMakerModelCardVersionSummary


class SageMakerListModelCardVersionsResponse(BaseModel):
    ModelCardVersionSummaryList: list[SageMakerModelCardVersionSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
