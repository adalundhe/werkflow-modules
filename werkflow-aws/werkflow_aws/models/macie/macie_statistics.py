from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class MacieStatistics(BaseModel):
    approximateNumberOfObjectsToProcess: StrictFloat | StrictInt | None = None
    numberOfRuns: StrictFloat | StrictInt | None = None
