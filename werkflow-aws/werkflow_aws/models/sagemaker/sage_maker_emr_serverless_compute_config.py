from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerEmrServerlessComputeConfig(BaseModel):
    ExecutionRoleARN: StrictStr | None = None
