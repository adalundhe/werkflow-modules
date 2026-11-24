from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_model_metadata_filter import SageMakerModelMetadataFilter


class SageMakerModelMetadataSearchExpression(BaseModel):
    Filters: list[SageMakerModelMetadataFilter] | None = None
