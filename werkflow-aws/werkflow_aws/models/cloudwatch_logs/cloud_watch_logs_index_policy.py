from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsIndexPolicy(BaseModel):
    logGroupIdentifier: StrictStr | None = None
    lastUpdateTime: StrictInt | None = None
    policyDocument: StrictStr | None = None
    policyName: StrictStr | None = None
    source: StrictStr | None = None
