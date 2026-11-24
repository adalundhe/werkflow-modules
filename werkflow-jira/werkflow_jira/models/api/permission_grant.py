from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from .permission_holder import PermissionHolder


class PermissionGrant(BaseModel):
    model_config = ConfigDict(extra="allow")

    holder: PermissionHolder | None = None
    id: StrictInt | None = None
    permission: StrictStr | None = None
    self: StrictStr | None = None
