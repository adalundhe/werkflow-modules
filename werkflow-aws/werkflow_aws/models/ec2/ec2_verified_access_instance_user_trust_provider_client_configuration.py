from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2VerifiedAccessInstanceUserTrustProviderClientConfiguration(BaseModel):
    Type: StrictStr | None = None
    Scopes: StrictStr | None = None
    Issuer: StrictStr | None = None
    AuthorizationEndpoint: StrictStr | None = None
    PublicSigningKeyEndpoint: StrictStr | None = None
    TokenEndpoint: StrictStr | None = None
    UserInfoEndpoint: StrictStr | None = None
    ClientId: StrictStr | None = None
    ClientSecret: StrictStr | None = None
    PkceEnabled: StrictBool | None = None
