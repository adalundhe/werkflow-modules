from __future__ import annotations
from pydantic import BaseModel, StrictStr, StrictInt
from .credentials import Credentials as _CredentialsModel
from .role_user import RoleUser


class AssumedRoleResponse(BaseModel):
    Credentials: _CredentialsModel | None = None
    AssumedRoleUser: RoleUser | None = None
    PackedPolicySize: StrictInt | None = None
    SourceIdentity: StrictStr | None = None
