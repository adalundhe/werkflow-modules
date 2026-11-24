from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_idp_client_authentication_result_type import CognitoIDPClientAuthenticationResultType


class CognitoIDPGetClientTokenResponse(BaseModel):
    ClientAuthenticationResult: CognitoIDPClientAuthenticationResultType | None = None
    ResponseMetadata: dict[str, Any] | None = None
