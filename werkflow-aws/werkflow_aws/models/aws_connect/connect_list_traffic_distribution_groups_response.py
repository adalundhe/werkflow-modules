from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_traffic_distribution_group_summary import ConnectTrafficDistributionGroupSummary


class ConnectListTrafficDistributionGroupsResponse(BaseModel):
    NextToken: StrictStr | None = None
    TrafficDistributionGroupSummaryList: list[ConnectTrafficDistributionGroupSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
