from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class SESPlacementStatistics(BaseModel):
    InboxPercentage: StrictFloat | StrictInt | None = None
    SpamPercentage: StrictFloat | StrictInt | None = None
    MissingPercentage: StrictFloat | StrictInt | None = None
    SpfPercentage: StrictFloat | StrictInt | None = None
    DkimPercentage: StrictFloat | StrictInt | None = None
