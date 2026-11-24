from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDescribeScanJobRequest(BaseModel):
    ScanJobId: StrictStr
