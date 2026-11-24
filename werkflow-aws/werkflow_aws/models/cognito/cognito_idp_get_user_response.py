from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_idp_attribute_type import CognitoIDPAttributeType
from .cognito_idpmfa_option_type import CognitoIDPMFAOptionType


class CognitoIDPGetUserResponse(BaseModel):
    Username: StrictStr | None = None
    UserAttributes: list[CognitoIDPAttributeType] | None = None
    MFAOptions: list[CognitoIDPMFAOptionType] | None = None
    PreferredMfaSetting: StrictStr | None = None
    UserMFASettingList: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
