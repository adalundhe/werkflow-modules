from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .backup_protected_resource_conditions import BackupProtectedResourceConditions


class BackupRestoreTestingSelectionForUpdate(BaseModel):
    IamRoleArn: StrictStr | None = None
    ProtectedResourceArns: list[StrictStr] | None = None
    ProtectedResourceConditions: BackupProtectedResourceConditions | None = None
    RestoreMetadataOverrides: dict[StrictStr, StrictStr] | None = None
    ValidationWindowHours: StrictInt | None = None
