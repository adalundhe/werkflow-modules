from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsOpenIdConnectGroupConfiguration(BaseModel):
    groupClaim: StrictStr
    groupEntityType: StrictStr
