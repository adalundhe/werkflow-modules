from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .batch_fairshare_utilization_detail import BatchFairshareUtilizationDetail
from .batch_queue_snapshot_capacity_usage import BatchQueueSnapshotCapacityUsage
from .batch_quota_share_utilization_detail import BatchQuotaShareUtilizationDetail


class BatchQueueSnapshotUtilizationDetail(BaseModel):
    totalCapacityUsage: list[BatchQueueSnapshotCapacityUsage] | None = None
    fairshareUtilization: BatchFairshareUtilizationDetail | None = None
    quotaShareUtilization: BatchQuotaShareUtilizationDetail | None = None
    lastUpdatedAt: StrictInt | None = None
