from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_permission_configuration import GuardDutyPermissionConfiguration


class GuardDutyPublicAccess(BaseModel):
    PermissionConfiguration: GuardDutyPermissionConfiguration | None = None
    EffectivePermission: StrictStr | None = None
