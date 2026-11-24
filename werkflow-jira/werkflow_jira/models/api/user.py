from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .avatar_urls_bean import AvatarUrlsBean
from .simple_list_wrapper_application_role import SimpleListWrapperApplicationRole
from .simple_list_wrapper_group_name import SimpleListWrapperGroupName


class User(BaseModel):
    accountId: StrictStr | None = None
    accountType: StrictStr | None = None
    active: StrictBool | None = None
    appType: StrictStr | None = None
    applicationRoles: SimpleListWrapperApplicationRole | None = None
    avatarUrls: AvatarUrlsBean | None = None
    displayName: StrictStr | None = None
    emailAddress: StrictStr | None = None
    expand: StrictStr | None = None
    groups: SimpleListWrapperGroupName | None = None
    guest: StrictBool | None = None
    key: StrictStr | None = None
    locale: StrictStr | None = None
    name: StrictStr | None = None
    self: StrictStr | None = None
    timeZone: StrictStr | None = None
