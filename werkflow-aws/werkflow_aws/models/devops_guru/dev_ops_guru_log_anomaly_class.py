from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class DevOpsGuruLogAnomalyClass(BaseModel):
    LogStreamName: StrictStr | None = None
    LogAnomalyType: StrictStr | None = None
    LogAnomalyToken: StrictStr | None = None
    LogEventId: StrictStr | None = None
    Explanation: StrictStr | None = None
    NumberOfLogLinesOccurrences: StrictInt | None = None
    LogEventTimestamp: datetime.datetime | StrictStr | None = None
