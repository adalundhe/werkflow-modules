from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerOptimizationSageMakerModel(BaseModel):
    ModelName: StrictStr | None = None
