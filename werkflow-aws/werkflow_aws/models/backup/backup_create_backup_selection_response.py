from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class BackupCreateBackupSelectionResponse(BaseModel):
    SelectionId: StrictStr | None = None
    BackupPlanId: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
