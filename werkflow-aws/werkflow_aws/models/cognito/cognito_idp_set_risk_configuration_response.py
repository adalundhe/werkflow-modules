from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_idp_risk_configuration_type import CognitoIDPRiskConfigurationType


class CognitoIDPSetRiskConfigurationResponse(BaseModel):
    RiskConfiguration: CognitoIDPRiskConfigurationType | None = None
    ResponseMetadata: dict[str, Any] | None = None
