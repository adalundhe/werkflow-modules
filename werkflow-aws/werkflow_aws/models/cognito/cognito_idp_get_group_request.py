from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPGetGroupRequest(BaseModel):
    GroupName: StrictStr
    UserPoolId: StrictStr
