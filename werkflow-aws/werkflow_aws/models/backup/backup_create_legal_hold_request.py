from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_recovery_point_selection import BackupRecoveryPointSelection


class BackupCreateLegalHoldRequest(BaseModel):
    Title: StrictStr
    Description: StrictStr
    IdempotencyToken: StrictStr | None = None
    RecoveryPointSelection: BackupRecoveryPointSelection | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
