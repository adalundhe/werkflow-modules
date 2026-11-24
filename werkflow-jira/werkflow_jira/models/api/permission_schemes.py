from __future__ import annotations
from pydantic import BaseModel
from .permission_scheme import PermissionScheme


class PermissionSchemes(BaseModel):
    permissionSchemes: list[PermissionScheme] | None = None
