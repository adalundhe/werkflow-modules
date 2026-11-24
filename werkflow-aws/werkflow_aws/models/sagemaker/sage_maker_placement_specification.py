from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerPlacementSpecification(BaseModel):
    UltraServerId: StrictStr | None = None
    InstanceCount: StrictInt | None = None
