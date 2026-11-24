from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idp_sms_configuration_type import CognitoIDPSmsConfigurationType


class CognitoIDPSmsMfaConfigType(BaseModel):
    SmsAuthenticationMessage: StrictStr | None = None
    SmsConfiguration: CognitoIDPSmsConfigurationType | None = None
