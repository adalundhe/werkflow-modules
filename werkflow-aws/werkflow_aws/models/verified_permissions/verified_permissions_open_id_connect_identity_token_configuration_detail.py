from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsOpenIdConnectIdentityTokenConfigurationDetail(BaseModel):
    principalIdClaim: StrictStr | None = None
    clientIds: list[StrictStr] | None = None
