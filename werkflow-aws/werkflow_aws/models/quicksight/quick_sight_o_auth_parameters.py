from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_vpc_connection_properties import QuickSightVpcConnectionProperties


class QuickSightOAuthParameters(BaseModel):
    TokenProviderUrl: StrictStr | None = None
    OAuthScope: StrictStr | None = None
    IdentityProviderVpcConnectionProperties: QuickSightVpcConnectionProperties | None = None
    IdentityProviderResourceUri: StrictStr | None = None
    IdentityProviderCACertificatesBundleS3Uri: StrictStr | None = None
