from typing import Dict

from pydantic import AnyHttpUrl, BaseModel, EmailStr, StrictBool, StrictStr


class JiraUser(BaseModel):
    self: AnyHttpUrl
    displayName: StrictStr
    accountId: StrictStr
    accountType: StrictStr
    emailAddress: EmailStr
    avatarUrls: Dict[StrictStr, AnyHttpUrl]
    active: StrictBool
    timeZone: StrictStr
    locale: StrictStr
