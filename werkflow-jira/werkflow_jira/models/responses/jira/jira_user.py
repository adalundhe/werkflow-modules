from typing import Dict

from pydantic import AnyHttpUrl, BaseModel, StrictBool, StrictStr


class JiraUser(BaseModel):
    self: AnyHttpUrl
    displayName: StrictStr
    accountId: StrictStr
    accountType: StrictStr
    emailAddress: StrictStr | None = None
    avatarUrls: Dict[StrictStr, AnyHttpUrl]
    active: StrictBool
    timeZone: StrictStr | None = None
    locale: StrictStr | None = None
