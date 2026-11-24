from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsTransformedLogRecord(BaseModel):
    eventNumber: StrictInt | None = None
    eventMessage: StrictStr | None = None
    transformedEventMessage: StrictStr | None = None
