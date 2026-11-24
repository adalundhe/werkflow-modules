from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_impersonated_user import GuardDutyImpersonatedUser


class GuardDutyKubernetesUserDetails(BaseModel):
    Username: StrictStr | None = None
    Uid: StrictStr | None = None
    Groups: list[StrictStr] | None = None
    SessionName: list[StrictStr] | None = None
    ImpersonatedUser: GuardDutyImpersonatedUser | None = None
