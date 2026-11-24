from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class QuickSightUser(BaseModel):
    Arn: StrictStr | None = None
    UserName: StrictStr | None = None
    Email: StrictStr | None = None
    Role: StrictStr | None = None
    IdentityType: StrictStr | None = None
    Active: StrictBool | None = None
    PrincipalId: StrictStr | None = None
    CustomPermissionsName: StrictStr | None = None
    ExternalLoginFederationProviderType: StrictStr | None = None
    ExternalLoginFederationProviderUrl: StrictStr | None = None
    ExternalLoginId: StrictStr | None = None
