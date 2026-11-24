from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchDeleteComputeEnvironmentRequest(BaseModel):
    computeEnvironment: StrictStr
