from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .quick_sight_authorization_code_grant_credentials_details import QuickSightAuthorizationCodeGrantCredentialsDetails


class QuickSightAuthorizationCodeGrantMetadata(BaseModel):
    BaseEndpoint: StrictStr
    RedirectUrl: StrictStr
    AuthorizationCodeGrantCredentialsSource: Literal['PLAIN_CREDENTIALS'] | None = None
    AuthorizationCodeGrantCredentialsDetails: QuickSightAuthorizationCodeGrantCredentialsDetails | None = None
