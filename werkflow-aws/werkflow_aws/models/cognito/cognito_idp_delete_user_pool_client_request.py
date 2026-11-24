from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDeleteUserPoolClientRequest(BaseModel):
    UserPoolId: StrictStr
    ClientId: StrictStr
