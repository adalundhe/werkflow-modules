from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightExternalIdpConfidentialAuthCodeAuthorizingConfigUpdateInput(BaseModel):
    ClientId: StrictStr
    IssuerUrl: StrictStr
