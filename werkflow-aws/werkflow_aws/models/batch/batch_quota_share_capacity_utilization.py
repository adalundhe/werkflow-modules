from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .batch_quota_share_capacity_usage import BatchQuotaShareCapacityUsage


class BatchQuotaShareCapacityUtilization(BaseModel):
    quotaShareName: StrictStr | None = None
    capacityUsage: list[BatchQuotaShareCapacityUsage] | None = None
