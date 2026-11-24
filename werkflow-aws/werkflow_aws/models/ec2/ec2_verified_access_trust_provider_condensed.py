from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2VerifiedAccessTrustProviderCondensed(BaseModel):
    VerifiedAccessTrustProviderId: StrictStr | None = None
    Description: StrictStr | None = None
    TrustProviderType: StrictStr | None = None
    UserTrustProviderType: StrictStr | None = None
    DeviceTrustProviderType: StrictStr | None = None
