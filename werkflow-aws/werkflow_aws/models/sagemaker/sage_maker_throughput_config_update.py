from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt


class SageMakerThroughputConfigUpdate(BaseModel):
    ThroughputMode: Literal['OnDemand', 'Provisioned'] | None = None
    ProvisionedReadCapacityUnits: StrictInt | None = None
    ProvisionedWriteCapacityUnits: StrictInt | None = None
