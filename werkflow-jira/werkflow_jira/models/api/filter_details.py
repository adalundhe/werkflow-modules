from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .filter_subscription import FilterSubscription
from .share_permission import SharePermission
from .user import User


class FilterDetails(BaseModel):
    approximateLastUsed: StrictStr | None = None
    description: StrictStr | None = None
    editPermissions: list[SharePermission] | None = None
    expand: StrictStr | None = None
    favourite: StrictBool | None = None
    favouritedCount: StrictInt | None = None
    id: StrictStr | None = None
    jql: StrictStr | None = None
    name: StrictStr | None = None
    owner: User | None = None
    searchUrl: StrictStr | None = None
    self: StrictStr | None = None
    sharePermissions: list[SharePermission] | None = None
    subscriptions: list[FilterSubscription] | None = None
    viewUrl: StrictStr | None = None
