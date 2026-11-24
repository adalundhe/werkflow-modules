from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_subscription_target_summary import DataZoneSubscriptionTargetSummary


class DataZoneListSubscriptionTargetsResponse(BaseModel):
    items: list[DataZoneSubscriptionTargetSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
