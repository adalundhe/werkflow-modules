from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class CostExplorerRootCauseImpact(BaseModel):
    Contribution: StrictFloat | StrictInt | None = None
