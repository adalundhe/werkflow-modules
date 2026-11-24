from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_compute_quota_summary import SageMakerComputeQuotaSummary


class SageMakerListComputeQuotasResponse(BaseModel):
    ComputeQuotaSummaries: list[SageMakerComputeQuotaSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
