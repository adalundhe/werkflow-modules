from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ELBv2AuthenticateOidcActionConfig(BaseModel):
    Issuer: StrictStr | None = None
    AuthorizationEndpoint: StrictStr | None = None
    TokenEndpoint: StrictStr | None = None
    UserInfoEndpoint: StrictStr | None = None
    ClientId: StrictStr | None = None
    ClientSecret: StrictStr | None = None
    SessionCookieName: StrictStr | None = None
    Scope: StrictStr | None = None
    SessionTimeout: StrictInt | None = None
    AuthenticationRequestExtraParams: dict[StrictStr, StrictStr] | None = None
    OnUnauthenticatedRequest: StrictStr | None = None
    UseExistingClientSecret: StrictBool | None = None
