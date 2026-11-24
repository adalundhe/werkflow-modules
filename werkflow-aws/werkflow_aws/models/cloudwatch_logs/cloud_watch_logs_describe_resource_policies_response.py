from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_resource_policy import CloudWatchLogsResourcePolicy


class CloudWatchLogsDescribeResourcePoliciesResponse(BaseModel):
    resourcePolicies: list[CloudWatchLogsResourcePolicy] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
