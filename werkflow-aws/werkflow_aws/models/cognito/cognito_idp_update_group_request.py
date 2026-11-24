from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPUpdateGroupRequest(BaseModel):
    GroupName: StrictStr
    UserPoolId: StrictStr
    Description: StrictStr | None = None
    RoleArn: StrictStr | None = None
    Precedence: StrictInt | None = None
