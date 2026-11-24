from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPListTermsRequest(BaseModel):
    UserPoolId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
