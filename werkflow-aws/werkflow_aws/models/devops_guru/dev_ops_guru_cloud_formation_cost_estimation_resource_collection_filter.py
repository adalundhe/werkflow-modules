from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DevOpsGuruCloudFormationCostEstimationResourceCollectionFilter(BaseModel):
    StackNames: list[StrictStr] | None = None
