from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cognito_idp_account_takeover_risk_configuration_type import CognitoIDPAccountTakeoverRiskConfigurationType
from .cognito_idp_compromised_credentials_risk_configuration_type import CognitoIDPCompromisedCredentialsRiskConfigurationType
from .cognito_idp_risk_exception_configuration_type import CognitoIDPRiskExceptionConfigurationType


class CognitoIDPRiskConfigurationType(BaseModel):
    UserPoolId: StrictStr | None = None
    ClientId: StrictStr | None = None
    CompromisedCredentialsRiskConfiguration: CognitoIDPCompromisedCredentialsRiskConfigurationType | None = None
    AccountTakeoverRiskConfiguration: CognitoIDPAccountTakeoverRiskConfigurationType | None = None
    RiskExceptionConfiguration: CognitoIDPRiskExceptionConfigurationType | None = None
    LastModifiedDate: datetime.datetime | StrictStr | None = None
