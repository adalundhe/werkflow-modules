from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerExtensionNodeSummary(BaseModel):
    TotalCount: StrictInt | None = None
    ActiveCount: StrictInt | None = None
