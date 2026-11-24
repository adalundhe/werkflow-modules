from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_read_authorization_code_grant_credentials_details import QuickSightReadAuthorizationCodeGrantCredentialsDetails


class QuickSightReadAuthorizationCodeGrantMetadata(BaseModel):
    BaseEndpoint: StrictStr | None = None
    RedirectUrl: StrictStr | None = None
    ReadAuthorizationCodeGrantCredentialsDetails: QuickSightReadAuthorizationCodeGrantCredentialsDetails | None = None
    AuthorizationCodeGrantCredentialsSource: StrictStr | None = None
