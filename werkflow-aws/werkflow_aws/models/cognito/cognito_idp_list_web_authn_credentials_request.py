from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPListWebAuthnCredentialsRequest(BaseModel):
    AccessToken: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
