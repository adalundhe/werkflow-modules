from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteVerifiedAccessTrustProviderRequest(BaseModel):
    VerifiedAccessTrustProviderId: StrictStr
    DryRun: StrictBool | None = None
    ClientToken: StrictStr | None = None
