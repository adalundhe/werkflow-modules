from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .backup_protected_resource_conditions import BackupProtectedResourceConditions


class BackupRestoreTestingSelectionForGet(BaseModel):
    CreationTime: datetime.datetime | StrictStr | None = None
    CreatorRequestId: StrictStr | None = None
    IamRoleArn: StrictStr | None = None
    ProtectedResourceArns: list[StrictStr] | None = None
    ProtectedResourceConditions: BackupProtectedResourceConditions | None = None
    ProtectedResourceType: StrictStr | None = None
    RestoreMetadataOverrides: dict[StrictStr, StrictStr] | None = None
    RestoreTestingPlanName: StrictStr | None = None
    RestoreTestingSelectionName: StrictStr | None = None
    ValidationWindowHours: StrictInt | None = None
