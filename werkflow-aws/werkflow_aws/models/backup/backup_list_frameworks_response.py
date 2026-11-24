from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_framework import BackupFramework


class BackupListFrameworksResponse(BaseModel):
    Frameworks: list[BackupFramework] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
