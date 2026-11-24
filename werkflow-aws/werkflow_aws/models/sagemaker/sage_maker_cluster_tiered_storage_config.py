from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerClusterTieredStorageConfig(BaseModel):
    Mode: StrictStr | None = None
    InstanceMemoryAllocationPercentage: StrictInt | None = None
