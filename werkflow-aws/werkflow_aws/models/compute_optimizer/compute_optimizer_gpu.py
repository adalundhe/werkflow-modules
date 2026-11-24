from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ComputeOptimizerGpu(BaseModel):
    gpuCount: StrictInt | None = None
    gpuMemorySizeInMiB: StrictInt | None = None
