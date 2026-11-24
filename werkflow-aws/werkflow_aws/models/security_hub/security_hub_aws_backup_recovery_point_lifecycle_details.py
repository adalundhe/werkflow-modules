from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SecurityHubAwsBackupRecoveryPointLifecycleDetails(BaseModel):
    DeleteAfterDays: StrictInt | None = None
    MoveToColdStorageAfterDays: StrictInt | None = None
