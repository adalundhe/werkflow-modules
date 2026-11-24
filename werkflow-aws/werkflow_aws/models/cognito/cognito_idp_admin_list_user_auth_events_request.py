from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPAdminListUserAuthEventsRequest(BaseModel):
    UserPoolId: StrictStr
    Username: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
