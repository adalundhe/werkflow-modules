from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_idp_document import CognitoIDPDocument


class CognitoIDPStartWebAuthnRegistrationResponse(BaseModel):
    CredentialCreationOptions: CognitoIDPDocument | None = None
    ResponseMetadata: dict[str, Any] | None = None
