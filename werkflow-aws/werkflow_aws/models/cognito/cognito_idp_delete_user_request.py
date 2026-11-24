from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDeleteUserRequest(BaseModel):
    AccessToken: StrictStr
