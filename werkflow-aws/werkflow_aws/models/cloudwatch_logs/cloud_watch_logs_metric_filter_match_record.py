from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsMetricFilterMatchRecord(BaseModel):
    eventNumber: StrictInt | None = None
    eventMessage: StrictStr | None = None
    extractedValues: dict[StrictStr, StrictStr] | None = None
