from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .batch_fairshare_policy import BatchFairsharePolicy
from .batch_quota_share_policy import BatchQuotaSharePolicy


class BatchUpdateSchedulingPolicyRequest(BaseModel):
    arn: StrictStr
    quotaSharePolicy: BatchQuotaSharePolicy | None = None
    fairsharePolicy: BatchFairsharePolicy | None = None
