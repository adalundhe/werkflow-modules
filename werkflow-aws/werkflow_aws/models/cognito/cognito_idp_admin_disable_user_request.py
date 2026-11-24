from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPAdminDisableUserRequest(BaseModel):
    UserPoolId: StrictStr
    Username: StrictStr
