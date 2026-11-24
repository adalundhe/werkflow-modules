from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt


class SageMakerThroughputConfig(BaseModel):
    ThroughputMode: Literal['OnDemand', 'Provisioned']
    ProvisionedReadCapacityUnits: StrictInt | None = None
    ProvisionedWriteCapacityUnits: StrictInt | None = None
