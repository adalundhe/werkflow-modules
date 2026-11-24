from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from .group_name import GroupName
from .user_details import UserDetails


class NotificationRecipients(BaseModel):
    model_config = ConfigDict(extra="allow")

    assignee: StrictBool | None = None
    groupIds: list[StrictStr] | None = None
    groups: list[GroupName] | None = None
    reporter: StrictBool | None = None
    users: list[UserDetails] | None = None
    voters: StrictBool | None = None
    watchers: StrictBool | None = None
