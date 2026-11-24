from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerOidcConfig(BaseModel):
    ClientId: StrictStr
    ClientSecret: StrictStr
    Issuer: StrictStr
    AuthorizationEndpoint: StrictStr
    TokenEndpoint: StrictStr
    UserInfoEndpoint: StrictStr
    LogoutEndpoint: StrictStr
    JwksUri: StrictStr
    Scope: StrictStr | None = None
    AuthenticationRequestExtraParams: dict[StrictStr, StrictStr] | None = None
