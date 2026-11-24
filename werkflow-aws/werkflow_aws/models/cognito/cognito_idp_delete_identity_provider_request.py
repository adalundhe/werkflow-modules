from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDeleteIdentityProviderRequest(BaseModel):
    UserPoolId: StrictStr
    ProviderName: StrictStr
