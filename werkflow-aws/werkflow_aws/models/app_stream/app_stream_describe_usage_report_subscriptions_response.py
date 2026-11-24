from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_stream_usage_report_subscription import AppStreamUsageReportSubscription


class AppStreamDescribeUsageReportSubscriptionsResponse(BaseModel):
    UsageReportSubscriptions: list[AppStreamUsageReportSubscription] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
