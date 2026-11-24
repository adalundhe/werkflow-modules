from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_idp_authentication_result_type import CognitoIDPAuthenticationResultType


class CognitoIDPGetTokensFromRefreshTokenResponse(BaseModel):
    AuthenticationResult: CognitoIDPAuthenticationResultType | None = None
    ResponseMetadata: dict[str, Any] | None = None
