from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class AutoScalingMemoryGiBPerVCpuRequest(BaseModel):
    Min: StrictFloat | StrictInt | None = None
    Max: StrictFloat | StrictInt | None = None
