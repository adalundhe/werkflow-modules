from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerObjectiveStatusCounters(BaseModel):
    Succeeded: StrictInt | None = None
    Pending: StrictInt | None = None
    Failed: StrictInt | None = None
