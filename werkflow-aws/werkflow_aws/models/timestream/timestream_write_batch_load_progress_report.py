from __future__ import annotations
from pydantic import BaseModel, StrictInt


class TimestreamWriteBatchLoadProgressReport(BaseModel):
    RecordsProcessed: StrictInt | None = None
    RecordsIngested: StrictInt | None = None
    ParseFailures: StrictInt | None = None
    RecordIngestionFailures: StrictInt | None = None
    FileFailures: StrictInt | None = None
    BytesMetered: StrictInt | None = None
