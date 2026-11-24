from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupScanSetting(BaseModel):
    MalwareScanner: StrictStr | None = None
    ResourceTypes: list[StrictStr] | None = None
    ScannerRoleArn: StrictStr | None = None
