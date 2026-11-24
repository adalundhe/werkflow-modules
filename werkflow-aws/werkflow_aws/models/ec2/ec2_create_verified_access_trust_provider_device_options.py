from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2CreateVerifiedAccessTrustProviderDeviceOptions(BaseModel):
    TenantId: StrictStr | None = None
    PublicSigningKeyUrl: StrictStr | None = None
