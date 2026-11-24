from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_protected_resource import BackupProtectedResource


class BackupListProtectedResourcesResponse(BaseModel):
    Results: list[BackupProtectedResource] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
