from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class BackupScanResult(BaseModel):
    MalwareScanner: StrictStr | None = None
    ScanJobState: StrictStr | None = None
    LastScanTimestamp: datetime.datetime | StrictStr | None = None
    Findings: list[StrictStr] | None = None
