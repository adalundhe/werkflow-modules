from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerEBSResourceUtilization(BaseModel):
    EbsReadOpsPerSecond: StrictStr | None = None
    EbsWriteOpsPerSecond: StrictStr | None = None
    EbsReadBytesPerSecond: StrictStr | None = None
    EbsWriteBytesPerSecond: StrictStr | None = None
