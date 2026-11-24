from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerThroughputConfigDescription(BaseModel):
    ThroughputMode: StrictStr | None = None
    ProvisionedReadCapacityUnits: StrictInt | None = None
    ProvisionedWriteCapacityUnits: StrictInt | None = None
