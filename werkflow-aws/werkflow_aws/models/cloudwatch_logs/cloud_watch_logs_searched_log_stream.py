from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudWatchLogsSearchedLogStream(BaseModel):
    logStreamName: StrictStr | None = None
    searchedCompletely: StrictBool | None = None
