from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class QuickSightTopicRefreshSchedule(BaseModel):
    IsEnabled: StrictBool | None = None
    BasedOnSpiceSchedule: StrictBool | None = None
    StartingAt: datetime.datetime | StrictStr | None = None
    Timezone: StrictStr | None = None
    RepeatAt: StrictStr | None = None
    TopicScheduleType: StrictStr | None = None
