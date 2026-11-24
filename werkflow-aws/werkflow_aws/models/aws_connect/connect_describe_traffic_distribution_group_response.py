from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_traffic_distribution_group import ConnectTrafficDistributionGroup


class ConnectDescribeTrafficDistributionGroupResponse(BaseModel):
    TrafficDistributionGroup: ConnectTrafficDistributionGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None
