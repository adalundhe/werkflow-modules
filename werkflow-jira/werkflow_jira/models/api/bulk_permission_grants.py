from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bulk_project_permission_grants import BulkProjectPermissionGrants


class BulkPermissionGrants(BaseModel):
    globalPermissions: list[StrictStr] | None = None
    projectPermissions: list[BulkProjectPermissionGrants] | None = None
