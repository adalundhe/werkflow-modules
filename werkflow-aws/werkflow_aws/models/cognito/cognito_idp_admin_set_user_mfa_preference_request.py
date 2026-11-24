from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idp_email_mfa_settings_type import CognitoIDPEmailMfaSettingsType
from .cognito_idpsms_mfa_settings_type import CognitoIDPSMSMfaSettingsType
from .cognito_idp_software_token_mfa_settings_type import CognitoIDPSoftwareTokenMfaSettingsType
from .cognito_idp_web_authn_mfa_settings_type import CognitoIDPWebAuthnMfaSettingsType


class CognitoIDPAdminSetUserMFAPreferenceRequest(BaseModel):
    Username: StrictStr
    UserPoolId: StrictStr
    SMSMfaSettings: CognitoIDPSMSMfaSettingsType | None = None
    SoftwareTokenMfaSettings: CognitoIDPSoftwareTokenMfaSettingsType | None = None
    EmailMfaSettings: CognitoIDPEmailMfaSettingsType | None = None
    WebAuthnMfaSettings: CognitoIDPWebAuthnMfaSettingsType | None = None
