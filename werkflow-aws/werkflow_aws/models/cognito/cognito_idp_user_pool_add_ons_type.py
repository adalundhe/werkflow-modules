from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idp_advanced_security_additional_flows_type import CognitoIDPAdvancedSecurityAdditionalFlowsType


class CognitoIDPUserPoolAddOnsType(BaseModel):
    AdvancedSecurityMode: StrictStr | None = None
    AdvancedSecurityAdditionalFlows: CognitoIDPAdvancedSecurityAdditionalFlowsType | None = None
