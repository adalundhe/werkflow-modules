from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESMessageInsightsFilters(BaseModel):
    FromEmailAddress: list[StrictStr] | None = None
    Destination: list[StrictStr] | None = None
    Subject: list[StrictStr] | None = None
    Isp: list[StrictStr] | None = None
    TenantName: list[StrictStr] | None = None
    LastDeliveryEvent: list[StrictStr] | None = None
    LastEngagementEvent: list[StrictStr] | None = None
