from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_index_policy import CloudWatchLogsIndexPolicy


class CloudWatchLogsDescribeIndexPoliciesResponse(BaseModel):
    indexPolicies: list[CloudWatchLogsIndexPolicy] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
