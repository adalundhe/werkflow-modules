from __future__ import annotations
from pydantic import BaseModel
from .cognito_idp_limit_definition_type import CognitoIDPLimitDefinitionType


class CognitoIDPGetProvisionedLimitRequest(BaseModel):
    LimitDefinition: CognitoIDPLimitDefinitionType
