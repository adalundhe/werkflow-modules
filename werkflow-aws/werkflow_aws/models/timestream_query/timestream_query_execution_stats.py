from __future__ import annotations
from pydantic import BaseModel, StrictInt


class TimestreamQueryExecutionStats(BaseModel):
    ExecutionTimeInMillis: StrictInt | None = None
    DataWrites: StrictInt | None = None
    BytesMetered: StrictInt | None = None
    CumulativeBytesScanned: StrictInt | None = None
    RecordsIngested: StrictInt | None = None
    QueryResultRows: StrictInt | None = None
