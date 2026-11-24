from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_model_metadata_summary import SageMakerModelMetadataSummary


class SageMakerListModelMetadataResponse(BaseModel):
    ModelMetadataSummaries: list[SageMakerModelMetadataSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
