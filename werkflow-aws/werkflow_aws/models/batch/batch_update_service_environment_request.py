from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .batch_capacity_limit import BatchCapacityLimit


class BatchUpdateServiceEnvironmentRequest(BaseModel):
    serviceEnvironment: StrictStr
    state: Literal['ENABLED', 'DISABLED'] | None = None
    capacityLimits: list[BatchCapacityLimit] | None = None
