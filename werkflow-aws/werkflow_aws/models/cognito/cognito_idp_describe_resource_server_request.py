from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDescribeResourceServerRequest(BaseModel):
    UserPoolId: StrictStr
    Identifier: StrictStr
