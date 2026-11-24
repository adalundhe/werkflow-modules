from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bulk_project_permissions import BulkProjectPermissions


class BulkPermissionsRequestBean(BaseModel):
    accountId: StrictStr | None = None
    globalPermissions: list[StrictStr] | None = None
    projectPermissions: list[BulkProjectPermissions] | None = None
