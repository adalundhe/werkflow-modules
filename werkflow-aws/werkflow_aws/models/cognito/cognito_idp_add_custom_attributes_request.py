from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idp_schema_attribute_type import CognitoIDPSchemaAttributeType


class CognitoIDPAddCustomAttributesRequest(BaseModel):
    UserPoolId: StrictStr
    CustomAttributes: list[CognitoIDPSchemaAttributeType]
