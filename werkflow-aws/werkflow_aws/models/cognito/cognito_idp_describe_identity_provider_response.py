from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_idp_identity_provider_type import CognitoIDPIdentityProviderType


class CognitoIDPDescribeIdentityProviderResponse(BaseModel):
    IdentityProvider: CognitoIDPIdentityProviderType | None = None
    ResponseMetadata: dict[str, Any] | None = None
