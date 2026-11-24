from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteComputeQuotaRequest(BaseModel):
    ComputeQuotaId: StrictStr
