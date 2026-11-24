from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsUpdateOpenIdConnectGroupConfiguration(BaseModel):
    groupClaim: StrictStr
    groupEntityType: StrictStr
