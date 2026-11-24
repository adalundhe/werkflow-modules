from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_recovery_point_by_resource import BackupRecoveryPointByResource


class BackupListRecoveryPointsByResourceResponse(BaseModel):
    NextToken: StrictStr | None = None
    RecoveryPoints: list[BackupRecoveryPointByResource] | None = None
    ResponseMetadata: dict[str, Any] | None = None
