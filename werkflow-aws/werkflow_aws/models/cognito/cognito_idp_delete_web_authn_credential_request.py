from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDeleteWebAuthnCredentialRequest(BaseModel):
    AccessToken: StrictStr
    CredentialId: StrictStr
