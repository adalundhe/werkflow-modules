from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .batch_fairshare_capacity_usage import BatchFairshareCapacityUsage


class BatchFairshareCapacityUtilization(BaseModel):
    shareIdentifier: StrictStr | None = None
    capacityUsage: list[BatchFairshareCapacityUsage] | None = None
