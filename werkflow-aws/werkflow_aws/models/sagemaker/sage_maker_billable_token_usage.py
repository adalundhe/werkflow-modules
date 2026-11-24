from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerBillableTokenUsage(BaseModel):
    PrefillTokenCount: StrictInt | None = None
    SampleTokenCount: StrictInt | None = None
    TrainingTokenCount: StrictInt | None = None
