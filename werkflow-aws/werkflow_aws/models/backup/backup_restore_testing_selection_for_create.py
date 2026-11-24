from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .backup_protected_resource_conditions import BackupProtectedResourceConditions


class BackupRestoreTestingSelectionForCreate(BaseModel):
    IamRoleArn: StrictStr
    ProtectedResourceType: StrictStr
    RestoreTestingSelectionName: StrictStr
    ProtectedResourceArns: list[StrictStr] | None = None
    ProtectedResourceConditions: BackupProtectedResourceConditions | None = None
    RestoreMetadataOverrides: dict[StrictStr, StrictStr] | None = None
    ValidationWindowHours: StrictInt | None = None
