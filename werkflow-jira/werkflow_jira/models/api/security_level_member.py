from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from .permission_holder import PermissionHolder


class SecurityLevelMember(BaseModel):
    model_config = ConfigDict(extra="allow")

    holder: PermissionHolder | None = None
    id: StrictStr | None = None
    issueSecurityLevelId: StrictStr | None = None
    issueSecuritySchemeId: StrictStr | None = None
    managed: StrictBool | None = None
