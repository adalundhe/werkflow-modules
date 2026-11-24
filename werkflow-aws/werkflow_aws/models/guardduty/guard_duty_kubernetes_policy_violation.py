from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyKubernetesPolicyViolation(BaseModel):
    ViolationType: StrictStr | None = None
    AffectedResource: StrictStr | None = None
    Subject: StrictStr | None = None
    GrantedAccess: StrictStr | None = None
    ExposureVector: StrictStr | None = None
    MisconfigurationImpact: StrictStr | None = None
