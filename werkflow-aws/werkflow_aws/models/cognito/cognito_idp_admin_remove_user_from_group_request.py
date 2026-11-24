from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPAdminRemoveUserFromGroupRequest(BaseModel):
    UserPoolId: StrictStr
    Username: StrictStr
    GroupName: StrictStr
