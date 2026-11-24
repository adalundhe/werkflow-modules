from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SharePermissionInputBean(BaseModel):
    accountId: StrictStr | None = None
    groupId: StrictStr | None = None
    groupname: StrictStr | None = None
    projectId: StrictStr | None = None
    projectRoleId: StrictStr | None = None
    rights: StrictInt | None = None
    type: StrictStr | None = None
