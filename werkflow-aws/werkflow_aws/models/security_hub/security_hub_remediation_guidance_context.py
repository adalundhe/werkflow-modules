from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubRemediationGuidanceContext(BaseModel):
    ProblemStatement: StrictStr | None = None
    RiskAssessment: StrictStr | None = None
    AffectedScope: StrictStr | None = None
    Prerequisites: list[StrictStr] | None = None
