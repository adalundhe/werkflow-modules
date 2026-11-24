from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .sage_maker_capacity_size_type import SageMakerCapacitySizeType


class SageMakerCapacitySize(BaseModel):
    Type: SageMakerCapacitySizeType | None = None
    Value: StrictInt | None = None
