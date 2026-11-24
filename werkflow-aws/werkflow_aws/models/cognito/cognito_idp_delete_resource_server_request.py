from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDeleteResourceServerRequest(BaseModel):
    UserPoolId: StrictStr
    Identifier: StrictStr
