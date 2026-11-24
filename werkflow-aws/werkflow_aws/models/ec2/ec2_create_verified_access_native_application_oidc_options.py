from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2CreateVerifiedAccessNativeApplicationOidcOptions(BaseModel):
    PublicSigningKeyEndpoint: StrictStr | None = None
    Issuer: StrictStr | None = None
    AuthorizationEndpoint: StrictStr | None = None
    TokenEndpoint: StrictStr | None = None
    UserInfoEndpoint: StrictStr | None = None
    ClientId: StrictStr | None = None
    ClientSecret: StrictStr | None = None
    Scope: StrictStr | None = None
