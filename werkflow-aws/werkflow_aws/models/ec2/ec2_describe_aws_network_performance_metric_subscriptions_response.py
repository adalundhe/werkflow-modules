from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_subscription import EC2Subscription


class EC2DescribeAwsNetworkPerformanceMetricSubscriptionsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Subscriptions: list[EC2Subscription] | None = None
    ResponseMetadata: dict[str, Any] | None = None
