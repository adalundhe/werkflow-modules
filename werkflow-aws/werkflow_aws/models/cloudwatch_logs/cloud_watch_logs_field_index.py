from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsFieldIndex(BaseModel):
    logGroupIdentifier: StrictStr | None = None
    fieldIndexName: StrictStr | None = None
    lastScanTime: StrictInt | None = None
    firstEventTime: StrictInt | None = None
    lastEventTime: StrictInt | None = None
    type: StrictStr | None = None
    indexCategory: StrictStr | None = None
