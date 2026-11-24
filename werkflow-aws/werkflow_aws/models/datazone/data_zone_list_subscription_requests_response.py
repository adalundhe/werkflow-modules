from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_subscription_request_summary import DataZoneSubscriptionRequestSummary


class DataZoneListSubscriptionRequestsResponse(BaseModel):
    items: list[DataZoneSubscriptionRequestSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
