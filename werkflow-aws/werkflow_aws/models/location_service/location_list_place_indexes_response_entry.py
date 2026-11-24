from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LocationListPlaceIndexesResponseEntry(BaseModel):
    IndexName: StrictStr | None = None
    Description: StrictStr | None = None
    DataSource: StrictStr | None = None
    PricingPlan: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
