from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .share_permission import SharePermission


class DashboardDetails(BaseModel):
    description: StrictStr | None = None
    editPermissions: list[SharePermission] | None = None
    name: StrictStr | None = None
    sharePermissions: list[SharePermission] | None = None
