from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPUpdateCIMDPolicyRequest(BaseModel):
    UserPoolId: StrictStr
    CIMDPolicyId: StrictStr
    ClientId: StrictStr
    URLPatterns: list[StrictStr]
    PolicyName: StrictStr | None = None
    CacheDuration: StrictInt | None = None
