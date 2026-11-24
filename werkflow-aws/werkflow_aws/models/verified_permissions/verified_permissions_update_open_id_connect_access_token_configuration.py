from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsUpdateOpenIdConnectAccessTokenConfiguration(BaseModel):
    principalIdClaim: StrictStr | None = None
    audiences: list[StrictStr] | None = None
