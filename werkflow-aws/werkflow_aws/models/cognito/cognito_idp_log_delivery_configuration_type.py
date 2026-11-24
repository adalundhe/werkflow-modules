from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idp_log_configuration_type import CognitoIDPLogConfigurationType


class CognitoIDPLogDeliveryConfigurationType(BaseModel):
    UserPoolId: StrictStr | None = None
    LogConfigurations: list[CognitoIDPLogConfigurationType] | None = None
