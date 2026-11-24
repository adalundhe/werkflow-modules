from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSOidcIdentityProviderConfig(BaseModel):
    identityProviderConfigName: StrictStr | None = None
    identityProviderConfigArn: StrictStr | None = None
    clusterName: StrictStr | None = None
    issuerUrl: StrictStr | None = None
    clientId: StrictStr | None = None
    usernameClaim: StrictStr | None = None
    usernamePrefix: StrictStr | None = None
    groupsClaim: StrictStr | None = None
    groupsPrefix: StrictStr | None = None
    requiredClaims: dict[StrictStr, StrictStr] | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    status: StrictStr | None = None
