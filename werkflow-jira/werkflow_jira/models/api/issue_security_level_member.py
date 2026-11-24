from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .permission_holder import PermissionHolder


class IssueSecurityLevelMember(BaseModel):
    holder: PermissionHolder | None = None
    id: StrictInt | None = None
    issueSecurityLevelId: StrictInt | None = None
