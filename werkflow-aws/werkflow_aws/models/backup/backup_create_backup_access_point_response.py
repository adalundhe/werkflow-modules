from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class BackupCreateBackupAccessPointResponse(BaseModel):
    AccessPointArn: StrictStr | None = None
    Status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
