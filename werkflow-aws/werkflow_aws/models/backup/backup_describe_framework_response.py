from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_framework_control import BackupFrameworkControl


class BackupDescribeFrameworkResponse(BaseModel):
    FrameworkName: StrictStr | None = None
    FrameworkArn: StrictStr | None = None
    FrameworkDescription: StrictStr | None = None
    FrameworkControls: list[BackupFrameworkControl] | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    DeploymentStatus: StrictStr | None = None
    FrameworkStatus: StrictStr | None = None
    IdempotencyToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
