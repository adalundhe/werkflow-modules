from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyInvestigationActor(BaseModel):
    AccessKeyId: StrictStr | None = None
    PrincipalId: StrictStr | None = None
    UserName: StrictStr | None = None
    UserType: StrictStr | None = None
    UserAgent: StrictStr | None = None
