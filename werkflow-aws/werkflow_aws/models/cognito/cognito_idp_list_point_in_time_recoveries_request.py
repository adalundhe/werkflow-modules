from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPListPointInTimeRecoveriesRequest(BaseModel):
    UserPoolId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
