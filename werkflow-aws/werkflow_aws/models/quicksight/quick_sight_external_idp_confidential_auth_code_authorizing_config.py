from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_external_idp_confidential_client_secret import QuickSightExternalIdpConfidentialClientSecret


class QuickSightExternalIdpConfidentialAuthCodeAuthorizingConfig(BaseModel):
    ClientId: StrictStr | None = None
    IssuerUrl: StrictStr | None = None
    ClientSecrets: list[QuickSightExternalIdpConfidentialClientSecret] | None = None
