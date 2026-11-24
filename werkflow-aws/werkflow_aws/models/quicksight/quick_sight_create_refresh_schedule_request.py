from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_refresh_schedule import QuickSightRefreshSchedule


class QuickSightCreateRefreshScheduleRequest(BaseModel):
    DataSetId: StrictStr
    AwsAccountId: StrictStr
    Schedule: QuickSightRefreshSchedule
