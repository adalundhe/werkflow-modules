from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPGetUserAttributeVerificationCodeRequest(BaseModel):
    AccessToken: StrictStr
    AttributeName: StrictStr
    ClientMetadata: dict[StrictStr, StrictStr] | None = None
