from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_idp_client_sso_session_config_type import CognitoIDPClientSSOSessionConfigType


class CognitoIDPSetUserPoolClientSessionConfigurationResponse(BaseModel):
    UserPoolId: StrictStr | None = None
    ClientId: StrictStr | None = None
    SSOSession: CognitoIDPClientSSOSessionConfigType | None = None
    ResponseMetadata: dict[str, Any] | None = None
