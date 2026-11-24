from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class BackupRestoreTestingSelectionForList(BaseModel):
    CreationTime: datetime.datetime | StrictStr | None = None
    IamRoleArn: StrictStr | None = None
    ProtectedResourceType: StrictStr | None = None
    RestoreTestingPlanName: StrictStr | None = None
    RestoreTestingSelectionName: StrictStr | None = None
    ValidationWindowHours: StrictInt | None = None
