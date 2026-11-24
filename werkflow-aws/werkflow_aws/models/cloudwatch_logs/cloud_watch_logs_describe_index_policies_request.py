from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDescribeIndexPoliciesRequest(BaseModel):
    logGroupIdentifiers: list[StrictStr]
    nextToken: StrictStr | None = None
