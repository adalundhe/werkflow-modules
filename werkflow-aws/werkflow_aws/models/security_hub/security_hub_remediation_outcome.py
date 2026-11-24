from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SecurityHubRemediationOutcome(BaseModel):
    ResolvedFindingsCount: StrictInt | None = None
    SeverityReductionFindingsCount: StrictInt | None = None
    SeverityUnchangedCount: StrictInt | None = None
