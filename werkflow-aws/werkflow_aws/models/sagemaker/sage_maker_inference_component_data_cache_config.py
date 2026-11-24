from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SageMakerInferenceComponentDataCacheConfig(BaseModel):
    EnableCaching: StrictBool
