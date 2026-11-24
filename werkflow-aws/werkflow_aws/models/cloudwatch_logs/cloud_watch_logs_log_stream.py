from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsLogStream(BaseModel):
    logStreamName: StrictStr | None = None
    creationTime: StrictInt | None = None
    firstEventTimestamp: StrictInt | None = None
    lastEventTimestamp: StrictInt | None = None
    lastIngestionTime: StrictInt | None = None
    uploadSequenceToken: StrictStr | None = None
    arn: StrictStr | None = None
    storedBytes: StrictInt | None = None
