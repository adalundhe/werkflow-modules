from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_sso_identity import EKSSsoIdentity


class EKSArgoCdRoleMapping(BaseModel):
    role: StrictStr | None = None
    identities: list[EKSSsoIdentity] | None = None
