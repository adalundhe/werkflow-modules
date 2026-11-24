from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idp_attribute_type import CognitoIDPAttributeType


class CognitoIDPUpdateUserAttributesRequest(BaseModel):
    UserAttributes: list[CognitoIDPAttributeType]
    AccessToken: StrictStr
    ClientMetadata: dict[StrictStr, StrictStr] | None = None
