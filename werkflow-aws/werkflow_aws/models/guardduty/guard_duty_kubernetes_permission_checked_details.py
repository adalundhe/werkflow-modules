from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GuardDutyKubernetesPermissionCheckedDetails(BaseModel):
    Verb: StrictStr | None = None
    Resource: StrictStr | None = None
    Namespace: StrictStr | None = None
    Allowed: StrictBool | None = None
