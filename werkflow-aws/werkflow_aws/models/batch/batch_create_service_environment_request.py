from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .batch_capacity_limit import BatchCapacityLimit


class BatchCreateServiceEnvironmentRequest(BaseModel):
    serviceEnvironmentName: StrictStr
    serviceEnvironmentType: Literal['SAGEMAKER_TRAINING']
    capacityLimits: list[BatchCapacityLimit]
    state: Literal['ENABLED', 'DISABLED'] | None = None
    tags: dict[StrictStr, StrictStr] | None = None
