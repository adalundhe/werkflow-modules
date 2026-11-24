from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .batch_capacity_limit import BatchCapacityLimit


class BatchServiceEnvironmentDetail(BaseModel):
    serviceEnvironmentName: StrictStr | None = None
    serviceEnvironmentArn: StrictStr | None = None
    serviceEnvironmentType: StrictStr | None = None
    state: StrictStr | None = None
    status: StrictStr | None = None
    capacityLimits: list[BatchCapacityLimit] | None = None
    tags: dict[StrictStr, StrictStr] | None = None
