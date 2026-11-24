from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class BackupDeleteBackupPlanResponse(BaseModel):
    BackupPlanId: StrictStr | None = None
    BackupPlanArn: StrictStr | None = None
    DeletionDate: datetime.datetime | StrictStr | None = None
    VersionId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
