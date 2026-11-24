from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDescribeIdentityProviderRequest(BaseModel):
    UserPoolId: StrictStr
    ProviderName: StrictStr
