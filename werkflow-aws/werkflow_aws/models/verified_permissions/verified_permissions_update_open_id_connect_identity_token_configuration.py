from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsUpdateOpenIdConnectIdentityTokenConfiguration(BaseModel):
    principalIdClaim: StrictStr | None = None
    clientIds: list[StrictStr] | None = None
