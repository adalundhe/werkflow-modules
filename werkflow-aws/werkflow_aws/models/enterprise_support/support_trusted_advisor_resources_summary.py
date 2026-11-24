from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SupportTrustedAdvisorResourcesSummary(BaseModel):
    resourcesProcessed: StrictInt | None = None
    resourcesFlagged: StrictInt | None = None
    resourcesIgnored: StrictInt | None = None
    resourcesSuppressed: StrictInt | None = None
