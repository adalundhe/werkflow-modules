from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .cognito_idp_limit_definition_type import CognitoIDPLimitDefinitionType


class CognitoIDPLimitType(BaseModel):
    LimitDefinition: CognitoIDPLimitDefinitionType | None = None
    ProvisionedLimitValue: StrictInt | None = None
    FreeLimitValue: StrictInt | None = None
