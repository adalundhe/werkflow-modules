from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPAdminEnableUserRequest(BaseModel):
    UserPoolId: StrictStr
    Username: StrictStr
