from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .scope import Scope


class ProjectRoleDetails(BaseModel):
    admin: StrictBool | None = None
    default: StrictBool | None = None
    description: StrictStr | None = None
    id: StrictInt | None = None
    name: StrictStr | None = None
    roleConfigurable: StrictBool | None = None
    scope: Scope | None = None
    self: StrictStr | None = None
    translatedName: StrictStr | None = None
    type: StrictStr | None = None
