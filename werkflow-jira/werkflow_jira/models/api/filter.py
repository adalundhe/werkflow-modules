from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .filter_subscriptions_list import FilterSubscriptionsList
from .share_permission import SharePermission
from .user import User
from .user_list import UserList


class Filter(BaseModel):
    approximateLastUsed: StrictStr | None = None
    description: StrictStr | None = None
    editPermissions: list[SharePermission] | None = None
    favourite: StrictBool | None = None
    favouritedCount: StrictInt | None = None
    id: StrictStr | None = None
    jql: StrictStr | None = None
    name: StrictStr | None = None
    owner: User | None = None
    searchUrl: StrictStr | None = None
    self: StrictStr | None = None
    sharePermissions: list[SharePermission] | None = None
    sharedUsers: UserList | None = None
    subscriptions: FilterSubscriptionsList | None = None
    viewUrl: StrictStr | None = None
