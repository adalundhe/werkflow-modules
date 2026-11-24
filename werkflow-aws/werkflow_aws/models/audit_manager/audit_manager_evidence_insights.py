from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AuditManagerEvidenceInsights(BaseModel):
    noncompliantEvidenceCount: StrictInt | None = None
    compliantEvidenceCount: StrictInt | None = None
    inconclusiveEvidenceCount: StrictInt | None = None
