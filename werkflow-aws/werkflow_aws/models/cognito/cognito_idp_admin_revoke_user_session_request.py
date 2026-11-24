from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CognitoIDPAdminRevokeUserSessionRequest(BaseModel):
    UserPoolId: StrictStr
    Username: StrictStr
    SessionId: StrictStr
    RevokeAssociatedSessions: Literal['NONE', 'LINKED'] | None = None
