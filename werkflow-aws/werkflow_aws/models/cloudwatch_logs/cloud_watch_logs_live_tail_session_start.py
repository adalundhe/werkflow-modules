from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsLiveTailSessionStart(BaseModel):
    requestId: StrictStr | None = None
    sessionId: StrictStr | None = None
    logGroupIdentifiers: list[StrictStr] | None = None
    logStreamNames: list[StrictStr] | None = None
    logStreamNamePrefixes: list[StrictStr] | None = None
    logEventFilterPattern: StrictStr | None = None
