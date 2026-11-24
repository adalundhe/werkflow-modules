from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPAdminGetUserRequest(BaseModel):
    UserPoolId: StrictStr
    Username: StrictStr
