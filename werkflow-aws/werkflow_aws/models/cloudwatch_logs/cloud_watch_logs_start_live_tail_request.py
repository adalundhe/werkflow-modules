from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsStartLiveTailRequest(BaseModel):
    logGroupIdentifiers: list[StrictStr]
    logStreamNames: list[StrictStr] | None = None
    logStreamNamePrefixes: list[StrictStr] | None = None
    logEventFilterPattern: StrictStr | None = None
