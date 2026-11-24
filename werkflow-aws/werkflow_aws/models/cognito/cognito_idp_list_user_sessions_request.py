from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPListUserSessionsRequest(BaseModel):
    AccessToken: StrictStr
    NextToken: StrictStr | None = None
