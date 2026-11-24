from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupScanResultInfo(BaseModel):
    ScanResultStatus: StrictStr | None = None
