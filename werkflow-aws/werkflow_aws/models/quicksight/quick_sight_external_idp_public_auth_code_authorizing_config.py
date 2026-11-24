from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightExternalIdpPublicAuthCodeAuthorizingConfig(BaseModel):
    ClientId: StrictStr | None = None
    IssuerUrl: StrictStr | None = None
