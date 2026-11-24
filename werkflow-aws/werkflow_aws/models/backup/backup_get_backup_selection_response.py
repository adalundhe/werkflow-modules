from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_selection import BackupSelection as _BackupSelectionType


class BackupGetBackupSelectionResponse(BaseModel):
    BackupSelection: _BackupSelectionType | None = None
    SelectionId: StrictStr | None = None
    BackupPlanId: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    CreatorRequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
