from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_idp_user_pool_token_session_config_type import CognitoIDPUserPoolTokenSessionConfigType


class CognitoIDPSetUserPoolSessionConfigurationResponse(BaseModel):
    UserPoolId: StrictStr | None = None
    UserSessionTracking: StrictStr | None = None
    TokenSession: CognitoIDPUserPoolTokenSessionConfigType | None = None
    ResponseMetadata: dict[str, Any] | None = None
