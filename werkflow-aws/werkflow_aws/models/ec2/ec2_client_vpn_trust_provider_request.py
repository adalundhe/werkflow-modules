from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EC2ClientVpnTrustProviderRequest(BaseModel):
    TrustProviderType: Literal['crowdstrike', 'jamf', 'jumpcloud'] | None = None
    TenantId: StrictStr | None = None
    PublicSigningKeyUrl: StrictStr | None = None
