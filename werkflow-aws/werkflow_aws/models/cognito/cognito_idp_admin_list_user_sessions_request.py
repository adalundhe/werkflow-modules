from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPAdminListUserSessionsRequest(BaseModel):
    UserPoolId: StrictStr
    Username: StrictStr
    NextToken: StrictStr | None = None
