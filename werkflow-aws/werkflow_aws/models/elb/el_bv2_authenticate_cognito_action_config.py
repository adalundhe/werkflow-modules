from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ELBv2AuthenticateCognitoActionConfig(BaseModel):
    UserPoolArn: StrictStr | None = None
    UserPoolClientId: StrictStr | None = None
    UserPoolDomain: StrictStr | None = None
    SessionCookieName: StrictStr | None = None
    Scope: StrictStr | None = None
    SessionTimeout: StrictInt | None = None
    AuthenticationRequestExtraParams: dict[StrictStr, StrictStr] | None = None
    OnUnauthenticatedRequest: StrictStr | None = None
