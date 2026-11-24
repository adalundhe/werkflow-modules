from __future__ import annotations
from pydantic import BaseModel, StrictInt


class BatchServiceJobPreemptionConfiguration(BaseModel):
    preemptionRetriesBeforeTermination: StrictInt | None = None
