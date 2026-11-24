from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerOidcConfigForResponse(BaseModel):
    ClientId: StrictStr | None = None
    Issuer: StrictStr | None = None
    AuthorizationEndpoint: StrictStr | None = None
    TokenEndpoint: StrictStr | None = None
    UserInfoEndpoint: StrictStr | None = None
    LogoutEndpoint: StrictStr | None = None
    JwksUri: StrictStr | None = None
    Scope: StrictStr | None = None
    AuthenticationRequestExtraParams: dict[StrictStr, StrictStr] | None = None
