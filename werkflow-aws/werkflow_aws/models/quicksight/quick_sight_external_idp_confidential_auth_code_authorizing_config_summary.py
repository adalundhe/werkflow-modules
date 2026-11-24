from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightExternalIdpConfidentialAuthCodeAuthorizingConfigSummary(BaseModel):
    ClientId: StrictStr | None = None
    IssuerUrl: StrictStr | None = None
