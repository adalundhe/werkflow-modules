from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .cognito_idp_limit_definition_type import CognitoIDPLimitDefinitionType


class CognitoIDPUpdateProvisionedLimitRequest(BaseModel):
    LimitDefinition: CognitoIDPLimitDefinitionType
    RequestedLimitValue: StrictInt
