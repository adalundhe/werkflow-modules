from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPVerifyUserAttributeRequest(BaseModel):
    AccessToken: StrictStr
    AttributeName: StrictStr
    Code: StrictStr
