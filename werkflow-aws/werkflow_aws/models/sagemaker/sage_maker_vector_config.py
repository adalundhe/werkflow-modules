from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerVectorConfig(BaseModel):
    Dimension: StrictInt | None = None
