from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .batch_quota_share_capacity_limit import BatchQuotaShareCapacityLimit
from .batch_quota_share_preemption_configuration import BatchQuotaSharePreemptionConfiguration
from .batch_quota_share_resource_sharing_configuration import BatchQuotaShareResourceSharingConfiguration


class BatchUpdateQuotaShareRequest(BaseModel):
    quotaShareArn: StrictStr
    capacityLimits: list[BatchQuotaShareCapacityLimit] | None = None
    resourceSharingConfiguration: BatchQuotaShareResourceSharingConfiguration | None = None
    preemptionConfiguration: BatchQuotaSharePreemptionConfiguration | None = None
    state: Literal['ENABLED', 'DISABLED'] | None = None
