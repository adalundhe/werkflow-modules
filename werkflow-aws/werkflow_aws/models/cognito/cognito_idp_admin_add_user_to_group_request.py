from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPAdminAddUserToGroupRequest(BaseModel):
    UserPoolId: StrictStr
    Username: StrictStr
    GroupName: StrictStr
