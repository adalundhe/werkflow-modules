from __future__ import annotations
from pydantic import BaseModel
from .batch_quota_share_capacity_utilization import BatchQuotaShareCapacityUtilization


class BatchQuotaShareUtilizationDetail(BaseModel):
    topCapacityUtilization: list[BatchQuotaShareCapacityUtilization] | None = None
