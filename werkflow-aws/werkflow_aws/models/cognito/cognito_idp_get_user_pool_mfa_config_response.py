from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_idp_email_mfa_config_type import CognitoIDPEmailMfaConfigType
from .cognito_idp_sms_mfa_config_type import CognitoIDPSmsMfaConfigType
from .cognito_idp_software_token_mfa_config_type import CognitoIDPSoftwareTokenMfaConfigType
from .cognito_idp_web_authn_configuration_type import CognitoIDPWebAuthnConfigurationType


class CognitoIDPGetUserPoolMfaConfigResponse(BaseModel):
    SmsMfaConfiguration: CognitoIDPSmsMfaConfigType | None = None
    SoftwareTokenMfaConfiguration: CognitoIDPSoftwareTokenMfaConfigType | None = None
    EmailMfaConfiguration: CognitoIDPEmailMfaConfigType | None = None
    MfaConfiguration: StrictStr | None = None
    WebAuthnConfiguration: CognitoIDPWebAuthnConfigurationType | None = None
    ResponseMetadata: dict[str, Any] | None = None
