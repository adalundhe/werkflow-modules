from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .sage_maker_capacity_size import SageMakerCapacitySize


class SageMakerRollingUpdatePolicy(BaseModel):
    MaximumBatchSize: SageMakerCapacitySize | None = None
    WaitIntervalInSeconds: StrictInt | None = None
    MaximumExecutionTimeoutInSeconds: StrictInt | None = None
    RollbackMaximumBatchSize: SageMakerCapacitySize | None = None
