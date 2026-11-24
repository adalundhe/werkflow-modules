from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BulkProjectPermissions(BaseModel):
    issues: list[StrictInt] | None = None
    permissions: list[StrictStr] | None = None
    projects: list[StrictInt] | None = None
