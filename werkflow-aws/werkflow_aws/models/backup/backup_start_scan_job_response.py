from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class BackupStartScanJobResponse(BaseModel):
    CreationDate: datetime.datetime | StrictStr | None = None
    ScanJobId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
