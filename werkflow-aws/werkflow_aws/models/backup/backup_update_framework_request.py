from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_framework_control import BackupFrameworkControl


class BackupUpdateFrameworkRequest(BaseModel):
    FrameworkName: StrictStr
    FrameworkDescription: StrictStr | None = None
    FrameworkControls: list[BackupFrameworkControl] | None = None
    IdempotencyToken: StrictStr | None = None
