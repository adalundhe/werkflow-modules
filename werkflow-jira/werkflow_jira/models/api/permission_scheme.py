from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from .permission_grant import PermissionGrant
from .scope import Scope


class PermissionScheme(BaseModel):
    model_config = ConfigDict(extra="allow")

    description: StrictStr | None = None
    expand: StrictStr | None = None
    id: StrictInt | None = None
    name: StrictStr | None = None
    permissions: list[PermissionGrant] | None = None
    scope: Scope | None = None
    self: StrictStr | None = None
