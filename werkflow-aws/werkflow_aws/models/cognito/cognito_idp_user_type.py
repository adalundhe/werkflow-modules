from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .cognito_idp_attribute_type import CognitoIDPAttributeType
from .cognito_idpmfa_option_type import CognitoIDPMFAOptionType


class CognitoIDPUserType(BaseModel):
    Username: StrictStr | None = None
    Attributes: list[CognitoIDPAttributeType] | None = None
    UserCreateDate: datetime.datetime | StrictStr | None = None
    UserLastModifiedDate: datetime.datetime | StrictStr | None = None
    Enabled: StrictBool | None = None
    UserStatus: StrictStr | None = None
    MFAOptions: list[CognitoIDPMFAOptionType] | None = None
