from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .batch_fairshare_policy import BatchFairsharePolicy
from .batch_quota_share_policy import BatchQuotaSharePolicy


class BatchCreateSchedulingPolicyRequest(BaseModel):
    name: StrictStr
    quotaSharePolicy: BatchQuotaSharePolicy | None = None
    fairsharePolicy: BatchFairsharePolicy | None = None
    tags: dict[StrictStr, StrictStr] | None = None
