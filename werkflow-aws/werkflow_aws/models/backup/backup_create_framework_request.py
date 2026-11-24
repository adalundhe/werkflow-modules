from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_framework_control import BackupFrameworkControl


class BackupCreateFrameworkRequest(BaseModel):
    FrameworkName: StrictStr
    FrameworkControls: list[BackupFrameworkControl]
    FrameworkDescription: StrictStr | None = None
    IdempotencyToken: StrictStr | None = None
    FrameworkTags: dict[StrictStr, StrictStr] | None = None
