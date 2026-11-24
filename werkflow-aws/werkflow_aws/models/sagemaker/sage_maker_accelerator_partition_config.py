from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerAcceleratorPartitionConfig(BaseModel):
    Type: StrictStr | None = None
    Count: StrictInt | None = None
