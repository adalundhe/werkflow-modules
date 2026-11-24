from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .avatar_urls_bean import AvatarUrlsBean


class UserDetails(BaseModel):
    accountId: StrictStr | None = None
    accountType: StrictStr | None = None
    active: StrictBool | None = None
    avatarUrls: AvatarUrlsBean | None = None
    displayName: StrictStr | None = None
    emailAddress: StrictStr | None = None
    key: StrictStr | None = None
    name: StrictStr | None = None
    self: StrictStr | None = None
    timeZone: StrictStr | None = None
