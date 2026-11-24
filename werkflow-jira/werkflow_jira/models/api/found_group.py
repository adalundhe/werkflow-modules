from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .group_label import GroupLabel


class FoundGroup(BaseModel):
    avatarUrl: StrictStr | None = None
    groupId: StrictStr | None = None
    html: StrictStr | None = None
    labels: list[GroupLabel] | None = None
    managedBy: StrictStr | None = None
    name: StrictStr | None = None
    usageType: StrictStr | None = None
