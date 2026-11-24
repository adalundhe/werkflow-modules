from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class BackupStartRestoreJobResponse(BaseModel):
    RestoreJobId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
