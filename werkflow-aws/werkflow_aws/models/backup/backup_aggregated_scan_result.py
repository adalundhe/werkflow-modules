from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class BackupAggregatedScanResult(BaseModel):
    FailedScan: StrictBool | None = None
    Findings: list[StrictStr] | None = None
    LastComputed: datetime.datetime | StrictStr | None = None
