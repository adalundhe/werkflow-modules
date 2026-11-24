from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .cognito_idp_number_attribute_constraints_type import CognitoIDPNumberAttributeConstraintsType
from .cognito_idp_string_attribute_constraints_type import CognitoIDPStringAttributeConstraintsType


class CognitoIDPSchemaAttributeType(BaseModel):
    Name: StrictStr | None = None
    AttributeDataType: StrictStr | None = None
    DeveloperOnlyAttribute: StrictBool | None = None
    Mutable: StrictBool | None = None
    Required: StrictBool | None = None
    NumberAttributeConstraints: CognitoIDPNumberAttributeConstraintsType | None = None
    StringAttributeConstraints: CognitoIDPStringAttributeConstraintsType | None = None
