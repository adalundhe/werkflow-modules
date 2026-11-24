from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerDescribeComputeQuotaRequest(BaseModel):
    ComputeQuotaId: StrictStr
    ComputeQuotaVersion: StrictInt | None = None
