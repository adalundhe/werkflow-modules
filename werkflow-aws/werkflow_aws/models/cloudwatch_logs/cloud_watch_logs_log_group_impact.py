from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsLogGroupImpact(BaseModel):
    logGroupName: StrictStr | None = None
    currentRetention: StrictStr | None = None
    proposedRetention: StrictStr | None = None
    storedBytes: StrictInt | None = None
