from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAcceleratorPartitionLayoutModel(BaseModel):
    AcceleratorPartitionTypes: list[StrictStr] | None = None
