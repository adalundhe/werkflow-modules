from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BulkProjectPermissionGrants(BaseModel):
    issues: list[StrictInt] | None = None
    permission: StrictStr | None = None
    projects: list[StrictInt] | None = None
