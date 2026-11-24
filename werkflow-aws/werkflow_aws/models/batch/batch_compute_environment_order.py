from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BatchComputeEnvironmentOrder(BaseModel):
    order: StrictInt | None = None
    computeEnvironment: StrictStr | None = None
