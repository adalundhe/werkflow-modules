from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class BackupGetRecoveryPointRestoreMetadataResponse(BaseModel):
    BackupVaultArn: StrictStr | None = None
    RecoveryPointArn: StrictStr | None = None
    RestoreMetadata: dict[StrictStr, StrictStr] | None = None
    ResourceType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
