from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ClientVpnTrustProvider(BaseModel):
    TrustProviderType: StrictStr | None = None
    TenantId: StrictStr | None = None
    PublicSigningKeyUrl: StrictStr | None = None
