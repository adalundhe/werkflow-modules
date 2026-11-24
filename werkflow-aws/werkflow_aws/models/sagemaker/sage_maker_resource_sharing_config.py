from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_compute_quota_resource_config import SageMakerComputeQuotaResourceConfig


class SageMakerResourceSharingConfig(BaseModel):
    Strategy: StrictStr | None = None
    BorrowLimit: StrictInt | None = None
    AbsoluteBorrowLimits: list[SageMakerComputeQuotaResourceConfig] | None = None
