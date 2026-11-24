from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyKubernetesRoleDetails(BaseModel):
    Kind: StrictStr | None = None
    Name: StrictStr | None = None
    Uid: StrictStr | None = None
