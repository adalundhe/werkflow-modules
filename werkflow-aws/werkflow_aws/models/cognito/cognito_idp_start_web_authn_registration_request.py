from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPStartWebAuthnRegistrationRequest(BaseModel):
    AccessToken: StrictStr
