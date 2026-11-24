from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class CostExplorerAnomalyScore(BaseModel):
    MaxScore: StrictFloat | StrictInt | None = None
    CurrentScore: StrictFloat | StrictInt | None = None
