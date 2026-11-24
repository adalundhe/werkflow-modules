from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SESExportStatistics(BaseModel):
    ProcessedRecordsCount: StrictInt | None = None
    ExportedRecordsCount: StrictInt | None = None
