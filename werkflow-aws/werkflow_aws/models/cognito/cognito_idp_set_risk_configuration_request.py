from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idp_account_takeover_risk_configuration_type import CognitoIDPAccountTakeoverRiskConfigurationType
from .cognito_idp_compromised_credentials_risk_configuration_type import CognitoIDPCompromisedCredentialsRiskConfigurationType
from .cognito_idp_risk_exception_configuration_type import CognitoIDPRiskExceptionConfigurationType


class CognitoIDPSetRiskConfigurationRequest(BaseModel):
    UserPoolId: StrictStr
    ClientId: StrictStr | None = None
    CompromisedCredentialsRiskConfiguration: CognitoIDPCompromisedCredentialsRiskConfigurationType | None = None
    AccountTakeoverRiskConfiguration: CognitoIDPAccountTakeoverRiskConfigurationType | None = None
    RiskExceptionConfiguration: CognitoIDPRiskExceptionConfigurationType | None = None
