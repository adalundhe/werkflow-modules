from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupScanAction(BaseModel):
    MalwareScanner: StrictStr | None = None
    ScanMode: StrictStr | None = None
