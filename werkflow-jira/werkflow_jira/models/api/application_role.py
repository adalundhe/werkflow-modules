from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .group_name import GroupName


class ApplicationRole(BaseModel):
    defaultGroups: list[StrictStr] | None = None
    defaultGroupsDetails: list[GroupName] | None = None
    defined: StrictBool | None = None
    groupDetails: list[GroupName] | None = None
    groups: list[StrictStr] | None = None
    hasUnlimitedSeats: StrictBool | None = None
    key: StrictStr | None = None
    name: StrictStr | None = None
    numberOfSeats: StrictInt | None = None
    platform: StrictBool | None = None
    remainingSeats: StrictInt | None = None
    selectedByDefault: StrictBool | None = None
    userCount: StrictInt | None = None
    userCountDescription: StrictStr | None = None
