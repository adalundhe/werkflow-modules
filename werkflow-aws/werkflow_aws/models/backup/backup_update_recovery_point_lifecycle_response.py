from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_calculated_lifecycle import BackupCalculatedLifecycle
from .backup_lifecycle import BackupLifecycle


class BackupUpdateRecoveryPointLifecycleResponse(BaseModel):
    BackupVaultArn: StrictStr | None = None
    RecoveryPointArn: StrictStr | None = None
    Lifecycle: BackupLifecycle | None = None
    CalculatedLifecycle: BackupCalculatedLifecycle | None = None
    ResponseMetadata: dict[str, Any] | None = None
