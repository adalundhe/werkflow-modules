from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_recovery_point_selection import BackupRecoveryPointSelection


class BackupGetLegalHoldResponse(BaseModel):
    Title: StrictStr | None = None
    Status: StrictStr | None = None
    Description: StrictStr | None = None
    CancelDescription: StrictStr | None = None
    LegalHoldId: StrictStr | None = None
    LegalHoldArn: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    CancellationDate: datetime.datetime | StrictStr | None = None
    RetainRecordUntil: datetime.datetime | StrictStr | None = None
    RecoveryPointSelection: BackupRecoveryPointSelection | None = None
    ResponseMetadata: dict[str, Any] | None = None
