from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2AddedPrincipal(BaseModel):
    PrincipalType: StrictStr | None = None
    Principal: StrictStr | None = None
    ServicePermissionId: StrictStr | None = None
    ServiceId: StrictStr | None = None
    PermissionType: StrictStr | None = None
