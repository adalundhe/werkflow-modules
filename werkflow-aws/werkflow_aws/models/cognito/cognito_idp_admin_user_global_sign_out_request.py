from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPAdminUserGlobalSignOutRequest(BaseModel):
    UserPoolId: StrictStr
    Username: StrictStr
