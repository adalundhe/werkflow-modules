from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .batch_front_of_quota_share_job_summary import BatchFrontOfQuotaShareJobSummary


class BatchFrontOfQuotaSharesDetail(BaseModel):
    quotaShares: dict[StrictStr, list[BatchFrontOfQuotaShareJobSummary]] | None = None
    lastUpdatedAt: StrictInt | None = None
