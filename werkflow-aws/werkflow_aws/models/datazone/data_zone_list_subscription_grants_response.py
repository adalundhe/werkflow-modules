from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_subscription_grant_summary import DataZoneSubscriptionGrantSummary


class DataZoneListSubscriptionGrantsResponse(BaseModel):
    items: list[DataZoneSubscriptionGrantSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
