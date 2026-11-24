from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_list_access_points_member import BackupListAccessPointsMember


class BackupListBackupAccessPointsResponse(BaseModel):
    BackupAccessPoints: list[BackupListAccessPointsMember] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
