from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .batch_quota_share_capacity_limit import BatchQuotaShareCapacityLimit
from .batch_quota_share_preemption_configuration import BatchQuotaSharePreemptionConfiguration
from .batch_quota_share_resource_sharing_configuration import BatchQuotaShareResourceSharingConfiguration


class BatchDescribeQuotaShareResponse(BaseModel):
    quotaShareName: StrictStr | None = None
    quotaShareArn: StrictStr | None = None
    jobQueueArn: StrictStr | None = None
    capacityLimits: list[BatchQuotaShareCapacityLimit] | None = None
    resourceSharingConfiguration: BatchQuotaShareResourceSharingConfiguration | None = None
    preemptionConfiguration: BatchQuotaSharePreemptionConfiguration | None = None
    state: StrictStr | None = None
    status: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
