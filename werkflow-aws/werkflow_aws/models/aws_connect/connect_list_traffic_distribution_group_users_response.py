from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_traffic_distribution_group_user_summary import ConnectTrafficDistributionGroupUserSummary


class ConnectListTrafficDistributionGroupUsersResponse(BaseModel):
    NextToken: StrictStr | None = None
    TrafficDistributionGroupUserSummaryList: list[ConnectTrafficDistributionGroupUserSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
