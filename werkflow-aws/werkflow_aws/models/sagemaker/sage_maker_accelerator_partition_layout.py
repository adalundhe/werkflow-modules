from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAcceleratorPartitionLayout(BaseModel):
    AcceleratorPartitionTypes: list[StrictStr] | None = None
