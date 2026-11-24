from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_user_account import SecurityHubUserAccount


class SecurityHubActorUser(BaseModel):
    Name: StrictStr | None = None
    Uid: StrictStr | None = None
    Type: StrictStr | None = None
    CredentialUid: StrictStr | None = None
    Account: SecurityHubUserAccount | None = None
