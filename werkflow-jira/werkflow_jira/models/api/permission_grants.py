from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .permission_grant import PermissionGrant


class PermissionGrants(BaseModel):
    expand: StrictStr | None = None
    permissions: list[PermissionGrant] | None = None
