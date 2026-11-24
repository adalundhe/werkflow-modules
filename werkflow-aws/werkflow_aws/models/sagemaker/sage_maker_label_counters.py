from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerLabelCounters(BaseModel):
    TotalLabeled: StrictInt | None = None
    HumanLabeled: StrictInt | None = None
    MachineLabeled: StrictInt | None = None
    FailedNonRetryableError: StrictInt | None = None
    Unlabeled: StrictInt | None = None
