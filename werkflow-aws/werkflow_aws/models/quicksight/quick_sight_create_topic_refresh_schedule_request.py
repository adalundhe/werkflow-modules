from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_topic_refresh_schedule import QuickSightTopicRefreshSchedule


class QuickSightCreateTopicRefreshScheduleRequest(BaseModel):
    AwsAccountId: StrictStr
    TopicId: StrictStr
    DatasetArn: StrictStr
    RefreshSchedule: QuickSightTopicRefreshSchedule
    DatasetName: StrictStr | None = None
