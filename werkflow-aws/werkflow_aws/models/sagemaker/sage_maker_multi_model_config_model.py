from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerMultiModelConfigModel(BaseModel):
    ModelCacheSetting: StrictStr | None = None
