from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDeleteGroupRequest(BaseModel):
    GroupName: StrictStr
    UserPoolId: StrictStr
