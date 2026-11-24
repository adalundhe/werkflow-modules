from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerDiskResourceUtilization(BaseModel):
    DiskReadOpsPerSecond: StrictStr | None = None
    DiskWriteOpsPerSecond: StrictStr | None = None
    DiskReadBytesPerSecond: StrictStr | None = None
    DiskWriteBytesPerSecond: StrictStr | None = None
