from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsGetLogGroupFieldsRequest(BaseModel):
    logGroupName: StrictStr | None = None
    time: StrictInt | None = None
    logGroupIdentifier: StrictStr | None = None
