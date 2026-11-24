from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDescribeCIMDPolicyRequest(BaseModel):
    UserPoolId: StrictStr
    CIMDPolicyId: StrictStr
