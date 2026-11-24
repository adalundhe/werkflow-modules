from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyKubernetesRoleBindingDetails(BaseModel):
    Kind: StrictStr | None = None
    Name: StrictStr | None = None
    Uid: StrictStr | None = None
    RoleRefName: StrictStr | None = None
    RoleRefKind: StrictStr | None = None
