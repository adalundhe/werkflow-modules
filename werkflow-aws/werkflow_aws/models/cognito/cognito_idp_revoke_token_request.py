from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CognitoIDPRevokeTokenRequest(BaseModel):
    Token: StrictStr
    ClientId: StrictStr
    ClientSecret: StrictStr | None = None
    RevokeAssociatedSessions: Literal['NONE', 'LINKED'] | None = None
