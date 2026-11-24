from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_model_cache_setting import SageMakerModelCacheSetting


class SageMakerMultiModelConfig(BaseModel):
    ModelCacheSetting: SageMakerModelCacheSetting | None = None
