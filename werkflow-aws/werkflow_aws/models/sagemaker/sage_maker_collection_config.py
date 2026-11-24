from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_vector_config import SageMakerVectorConfig


class SageMakerCollectionConfig(BaseModel):
    VectorConfig: SageMakerVectorConfig | None = None
