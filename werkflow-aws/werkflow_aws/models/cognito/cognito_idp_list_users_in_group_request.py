from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPListUsersInGroupRequest(BaseModel):
    UserPoolId: StrictStr
    GroupName: StrictStr
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
