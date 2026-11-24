from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SecurityHubAwsBackupBackupPlanLifecycleDetails(BaseModel):
    DeleteAfterDays: StrictInt | None = None
    MoveToColdStorageAfterDays: StrictInt | None = None
