from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDeleteUserPoolClientSecretRequest(BaseModel):
    UserPoolId: StrictStr
    ClientId: StrictStr
    ClientSecretId: StrictStr
