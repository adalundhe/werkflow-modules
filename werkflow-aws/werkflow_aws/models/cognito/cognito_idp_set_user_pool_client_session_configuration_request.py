from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idp_client_sso_session_config_type import CognitoIDPClientSSOSessionConfigType


class CognitoIDPSetUserPoolClientSessionConfigurationRequest(BaseModel):
    UserPoolId: StrictStr
    ClientId: StrictStr
    SSOSession: CognitoIDPClientSSOSessionConfigType
