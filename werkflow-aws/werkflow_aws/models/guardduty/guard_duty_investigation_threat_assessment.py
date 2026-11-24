from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_reputation import GuardDutyReputation


class GuardDutyInvestigationThreatAssessment(BaseModel):
    Reputation: GuardDutyReputation | None = None
    ThreatConfidence: StrictStr | None = None
    Classification: StrictStr | None = None
    Assessment: StrictStr | None = None
    AuthenticationContext: StrictStr | None = None
    RdsControlPlaneActivity: StrictStr | None = None
    IpAccountActivity: StrictStr | None = None
    CredentialCompromise: StrictStr | None = None
