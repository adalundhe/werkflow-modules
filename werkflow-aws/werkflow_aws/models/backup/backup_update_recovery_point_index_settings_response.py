from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class BackupUpdateRecoveryPointIndexSettingsResponse(BaseModel):
    BackupVaultName: StrictStr | None = None
    RecoveryPointArn: StrictStr | None = None
    IndexStatus: StrictStr | None = None
    Index: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
