from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_idp_web_authn_credential_description import CognitoIDPWebAuthnCredentialDescription


class CognitoIDPListWebAuthnCredentialsResponse(BaseModel):
    Credentials: list[CognitoIDPWebAuthnCredentialDescription] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
