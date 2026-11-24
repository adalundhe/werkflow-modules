from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class BackupLifecycle(BaseModel):
    MoveToColdStorageAfterDays: StrictInt | None = None
    DeleteAfterDays: StrictInt | None = None
    OptInToArchiveForSupportedResources: StrictBool | None = None
    DeleteAfterEvent: StrictStr | None = None
