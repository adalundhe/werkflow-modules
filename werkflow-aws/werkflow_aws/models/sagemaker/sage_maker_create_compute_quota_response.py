from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerCreateComputeQuotaResponse(BaseModel):
    ComputeQuotaArn: StrictStr | None = None
    ComputeQuotaId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
