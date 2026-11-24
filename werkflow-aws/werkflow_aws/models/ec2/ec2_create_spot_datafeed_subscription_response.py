from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_spot_datafeed_subscription import EC2SpotDatafeedSubscription


class EC2CreateSpotDatafeedSubscriptionResponse(BaseModel):
    SpotDatafeedSubscription: EC2SpotDatafeedSubscription | None = None
    ResponseMetadata: dict[str, Any] | None = None
