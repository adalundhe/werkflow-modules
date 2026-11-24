from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .group_name import GroupName
from .restricted_permission import RestrictedPermission


class NotificationRecipientsRestrictions(BaseModel):
    groupIds: list[StrictStr] | None = None
    groups: list[GroupName] | None = None
    permissions: list[RestrictedPermission] | None = None
