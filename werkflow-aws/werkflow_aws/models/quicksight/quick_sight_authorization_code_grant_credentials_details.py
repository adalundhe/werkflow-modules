from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_authorization_code_grant_details import QuickSightAuthorizationCodeGrantDetails


class QuickSightAuthorizationCodeGrantCredentialsDetails(BaseModel):
    AuthorizationCodeGrantDetails: QuickSightAuthorizationCodeGrantDetails | None = None
