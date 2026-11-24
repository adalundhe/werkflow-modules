from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerUpdateComputeQuotaResponse(BaseModel):
    ComputeQuotaArn: StrictStr | None = None
    ComputeQuotaVersion: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
