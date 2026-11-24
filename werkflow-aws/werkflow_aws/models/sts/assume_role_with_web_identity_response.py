from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .credentials import Credentials as _CredentialsModel
from .role_user import RoleUser


class AssumeRoleWithWebIdentityResponse(BaseModel):
    Credentials: _CredentialsModel | None = None
    SubjectFromWebIdentityToken: StrictStr | None = None
    AssumedRoleUser: RoleUser | None = None
    PackedPolicySize: StrictInt | None = None
    Provider: StrictStr | None = None
    Audience: StrictStr | None = None
    SourceIdentity: StrictStr | None = None
