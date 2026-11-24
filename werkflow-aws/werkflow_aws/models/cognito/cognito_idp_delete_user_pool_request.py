from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDeleteUserPoolRequest(BaseModel):
    UserPoolId: StrictStr
