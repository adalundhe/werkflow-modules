from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_idp_client_secret_input import QuickSightIdpClientSecretInput


class QuickSightExternalIdpConfidentialAuthCodeAuthorizingConfigInput(BaseModel):
    ClientId: StrictStr
    IssuerUrl: StrictStr
    ClientSecret: QuickSightIdpClientSecretInput
