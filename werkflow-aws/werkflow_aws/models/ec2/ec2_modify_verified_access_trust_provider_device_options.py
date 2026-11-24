from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ModifyVerifiedAccessTrustProviderDeviceOptions(BaseModel):
    PublicSigningKeyUrl: StrictStr | None = None
