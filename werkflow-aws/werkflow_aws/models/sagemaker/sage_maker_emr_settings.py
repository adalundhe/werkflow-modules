from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerEmrSettings(BaseModel):
    AssumableRoleArns: list[StrictStr] | None = None
    ExecutionRoleArns: list[StrictStr] | None = None
