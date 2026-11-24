from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .cognito_idp_attribute_type import CognitoIDPAttributeType
from .cognito_idpmfa_option_type import CognitoIDPMFAOptionType


class CognitoIDPAdminGetUserResponse(BaseModel):
    Username: StrictStr | None = None
    UserAttributes: list[CognitoIDPAttributeType] | None = None
    UserCreateDate: datetime.datetime | StrictStr | None = None
    UserLastModifiedDate: datetime.datetime | StrictStr | None = None
    Enabled: StrictBool | None = None
    UserStatus: StrictStr | None = None
    MFAOptions: list[CognitoIDPMFAOptionType] | None = None
    PreferredMfaSetting: StrictStr | None = None
    UserMFASettingList: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
