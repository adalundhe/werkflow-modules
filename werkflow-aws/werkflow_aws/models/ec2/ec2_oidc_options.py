from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2OidcOptions(BaseModel):
    Issuer: StrictStr | None = None
    AuthorizationEndpoint: StrictStr | None = None
    TokenEndpoint: StrictStr | None = None
    UserInfoEndpoint: StrictStr | None = None
    ClientId: StrictStr | None = None
    ClientSecret: StrictStr | None = None
    Scope: StrictStr | None = None
