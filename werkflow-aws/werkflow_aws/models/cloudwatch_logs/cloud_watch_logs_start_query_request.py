from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsStartQueryRequest(BaseModel):
    startTime: StrictInt
    endTime: StrictInt
    queryString: StrictStr
    queryLanguage: Literal['CWLI', 'SQL', 'PPL'] | None = None
    logGroupName: StrictStr | None = None
    logGroupNames: list[StrictStr] | None = None
    logGroupIdentifiers: list[StrictStr] | None = None
    limit: StrictInt | None = None
