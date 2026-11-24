from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_schedule_refresh_on_entity import QuickSightScheduleRefreshOnEntity


class QuickSightRefreshFrequency(BaseModel):
    Interval: StrictStr | None = None
    RefreshOnDay: QuickSightScheduleRefreshOnEntity | None = None
    Timezone: StrictStr | None = None
    TimeOfTheDay: StrictStr | None = None
