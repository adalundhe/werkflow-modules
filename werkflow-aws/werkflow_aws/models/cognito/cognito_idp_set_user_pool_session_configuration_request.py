from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .cognito_idp_user_pool_token_session_config_type import CognitoIDPUserPoolTokenSessionConfigType


class CognitoIDPSetUserPoolSessionConfigurationRequest(BaseModel):
    UserPoolId: StrictStr
    UserSessionTracking: Literal['ENABLED', 'DISABLED']
    TokenSession: CognitoIDPUserPoolTokenSessionConfigType
