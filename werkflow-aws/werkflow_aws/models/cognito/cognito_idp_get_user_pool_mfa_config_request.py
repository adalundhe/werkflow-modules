from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPGetUserPoolMfaConfigRequest(BaseModel):
    UserPoolId: StrictStr
