from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class SageMakerAutoMLDataSplitConfig(BaseModel):
    ValidationFraction: StrictFloat | StrictInt | None = None
