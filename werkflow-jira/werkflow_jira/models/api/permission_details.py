from __future__ import annotations
from pydantic import BaseModel
from .share_permission import SharePermission


class PermissionDetails(BaseModel):
    editPermissions: list[SharePermission] | None = None
    sharePermissions: list[SharePermission] | None = None
