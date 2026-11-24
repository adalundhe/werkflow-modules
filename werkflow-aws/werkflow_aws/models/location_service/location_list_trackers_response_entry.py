from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LocationListTrackersResponseEntry(BaseModel):
    TrackerName: StrictStr | None = None
    Description: StrictStr | None = None
    PricingPlan: StrictStr | None = None
    PricingPlanDataSource: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
