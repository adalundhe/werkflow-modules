from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idp_attribute_type import CognitoIDPAttributeType


class CognitoIDPAdminUpdateUserAttributesRequest(BaseModel):
    UserPoolId: StrictStr
    Username: StrictStr
    UserAttributes: list[CognitoIDPAttributeType]
    ClientMetadata: dict[StrictStr, StrictStr] | None = None
