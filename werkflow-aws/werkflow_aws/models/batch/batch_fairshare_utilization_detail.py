from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .batch_fairshare_capacity_utilization import BatchFairshareCapacityUtilization


class BatchFairshareUtilizationDetail(BaseModel):
    activeShareCount: StrictInt | None = None
    topCapacityUtilization: list[BatchFairshareCapacityUtilization] | None = None
