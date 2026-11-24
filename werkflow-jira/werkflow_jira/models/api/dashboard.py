from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .share_permission import SharePermission
from .user_bean import UserBean


class Dashboard(BaseModel):
    automaticRefreshMs: StrictInt | None = None
    description: StrictStr | None = None
    editPermissions: list[SharePermission] | None = None
    id: StrictStr | None = None
    isFavourite: StrictBool | None = None
    isWritable: StrictBool | None = None
    name: StrictStr | None = None
    owner: UserBean | None = None
    popularity: StrictInt | None = None
    rank: StrictInt | None = None
    self: StrictStr | None = None
    sharePermissions: list[SharePermission] | None = None
    systemDashboard: StrictBool | None = None
    view: StrictStr | None = None
