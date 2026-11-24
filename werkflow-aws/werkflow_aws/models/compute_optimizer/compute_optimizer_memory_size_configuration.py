from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ComputeOptimizerMemorySizeConfiguration(BaseModel):
    memory: StrictInt | None = None
    memoryReservation: StrictInt | None = None
