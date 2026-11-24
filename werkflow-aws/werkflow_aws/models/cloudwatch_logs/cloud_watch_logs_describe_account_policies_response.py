from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_account_policy import CloudWatchLogsAccountPolicy


class CloudWatchLogsDescribeAccountPoliciesResponse(BaseModel):
    accountPolicies: list[CloudWatchLogsAccountPolicy] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
