from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPCreateCIMDPolicyRequest(BaseModel):
    UserPoolId: StrictStr
    ClientId: StrictStr
    PolicyName: StrictStr
    URLPatterns: list[StrictStr]
    CacheDuration: StrictInt | None = None
