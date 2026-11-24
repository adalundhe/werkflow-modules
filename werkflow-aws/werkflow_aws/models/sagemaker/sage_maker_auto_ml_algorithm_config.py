from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAutoMLAlgorithmConfig(BaseModel):
    AutoMLAlgorithms: list[StrictStr] | None = None
