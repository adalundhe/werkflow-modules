from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idp_document import CognitoIDPDocument


class CognitoIDPCompleteWebAuthnRegistrationRequest(BaseModel):
    AccessToken: StrictStr
    Credential: CognitoIDPDocument
