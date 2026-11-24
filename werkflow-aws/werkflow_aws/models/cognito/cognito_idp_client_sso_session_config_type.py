from __future__ import annotations
from pydantic import BaseModel, StrictInt


class CognitoIDPClientSSOSessionConfigType(BaseModel):
    MaxValidityMinutes: StrictInt | None = None
