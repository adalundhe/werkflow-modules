from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_indexed_recovery_point import BackupIndexedRecoveryPoint


class BackupListIndexedRecoveryPointsResponse(BaseModel):
    IndexedRecoveryPoints: list[BackupIndexedRecoveryPoint] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
