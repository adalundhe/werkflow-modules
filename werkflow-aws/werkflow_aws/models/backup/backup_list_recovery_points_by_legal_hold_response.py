from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_recovery_point_member import BackupRecoveryPointMember


class BackupListRecoveryPointsByLegalHoldResponse(BaseModel):
    RecoveryPoints: list[BackupRecoveryPointMember] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
