from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsOpenIdConnectGroupConfigurationItem(BaseModel):
    groupClaim: StrictStr | None = None
    groupEntityType: StrictStr | None = None
