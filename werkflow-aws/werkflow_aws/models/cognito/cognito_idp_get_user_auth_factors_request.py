from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPGetUserAuthFactorsRequest(BaseModel):
    AccessToken: StrictStr
