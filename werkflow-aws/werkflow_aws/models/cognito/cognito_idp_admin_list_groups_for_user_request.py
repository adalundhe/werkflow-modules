from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPAdminListGroupsForUserRequest(BaseModel):
    Username: StrictStr
    UserPoolId: StrictStr
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
