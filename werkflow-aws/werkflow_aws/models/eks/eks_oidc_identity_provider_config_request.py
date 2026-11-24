from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSOidcIdentityProviderConfigRequest(BaseModel):
    identityProviderConfigName: StrictStr
    issuerUrl: StrictStr
    clientId: StrictStr
    usernameClaim: StrictStr | None = None
    usernamePrefix: StrictStr | None = None
    groupsClaim: StrictStr | None = None
    groupsPrefix: StrictStr | None = None
    requiredClaims: dict[StrictStr, StrictStr] | None = None
