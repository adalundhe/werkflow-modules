from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDescribeUserPoolClientRequest(BaseModel):
    UserPoolId: StrictStr
    ClientId: StrictStr
