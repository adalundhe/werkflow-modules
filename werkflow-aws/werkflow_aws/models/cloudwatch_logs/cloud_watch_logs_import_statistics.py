from __future__ import annotations
from pydantic import BaseModel, StrictInt


class CloudWatchLogsImportStatistics(BaseModel):
    bytesImported: StrictInt | None = None
