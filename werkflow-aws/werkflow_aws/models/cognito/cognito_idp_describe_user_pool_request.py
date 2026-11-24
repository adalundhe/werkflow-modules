from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDescribeUserPoolRequest(BaseModel):
    UserPoolId: StrictStr
