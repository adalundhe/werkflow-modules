from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt
from .cognito_idp_message_template_type import CognitoIDPMessageTemplateType


class CognitoIDPAdminCreateUserConfigType(BaseModel):
    AllowAdminCreateUserOnly: StrictBool | None = None
    UnusedAccountValidityDays: StrictInt | None = None
    InviteMessageTemplate: CognitoIDPMessageTemplateType | None = None
