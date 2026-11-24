from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .cognito_idp_attribute_type import CognitoIDPAttributeType


class CognitoIDPAdminCreateUserRequest(BaseModel):
    UserPoolId: StrictStr
    Username: StrictStr
    UserAttributes: list[CognitoIDPAttributeType] | None = None
    ValidationData: list[CognitoIDPAttributeType] | None = None
    TemporaryPassword: StrictStr | None = None
    ForceAliasCreation: StrictBool | None = None
    MessageAction: Literal['RESEND', 'SUPPRESS'] | None = None
    DesiredDeliveryMediums: list[Literal['SMS', 'EMAIL']] | None = None
    ClientMetadata: dict[StrictStr, StrictStr] | None = None
