from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .user_permission import UserPermission


class Permissions(BaseModel):
    permissions: dict[StrictStr, UserPermission] | None = None
