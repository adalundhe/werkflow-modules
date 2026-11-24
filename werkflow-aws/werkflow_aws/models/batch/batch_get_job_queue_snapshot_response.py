from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .batch_front_of_queue_detail import BatchFrontOfQueueDetail
from .batch_front_of_quota_shares_detail import BatchFrontOfQuotaSharesDetail
from .batch_queue_snapshot_utilization_detail import BatchQueueSnapshotUtilizationDetail


class BatchGetJobQueueSnapshotResponse(BaseModel):
    frontOfQueue: BatchFrontOfQueueDetail | None = None
    frontOfQuotaShares: BatchFrontOfQuotaSharesDetail | None = None
    queueUtilization: BatchQueueSnapshotUtilizationDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
