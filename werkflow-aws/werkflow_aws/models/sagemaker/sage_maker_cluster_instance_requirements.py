from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerClusterInstanceRequirements(BaseModel):
    InstanceTypes: list[StrictStr]
