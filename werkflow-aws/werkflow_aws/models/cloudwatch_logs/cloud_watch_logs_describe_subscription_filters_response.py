from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_subscription_filter import CloudWatchLogsSubscriptionFilter


class CloudWatchLogsDescribeSubscriptionFiltersResponse(BaseModel):
    subscriptionFilters: list[CloudWatchLogsSubscriptionFilter] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
