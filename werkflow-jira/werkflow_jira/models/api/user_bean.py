from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .user_bean_avatar_urls import UserBeanAvatarUrls


class UserBean(BaseModel):
    accountId: StrictStr | None = None
    active: StrictBool | None = None
    avatarUrls: UserBeanAvatarUrls | None = None
    displayName: StrictStr | None = None
    key: StrictStr | None = None
    name: StrictStr | None = None
    self: StrictStr | None = None
