from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CloudWatchAlarmHistoryItem(BaseModel):
    AlarmName: StrictStr | None = None
    AlarmContributorId: StrictStr | None = None
    AlarmType: StrictStr | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
    HistoryItemType: StrictStr | None = None
    HistorySummary: StrictStr | None = None
    HistoryData: StrictStr | None = None
    AlarmContributorAttributes: dict[StrictStr, StrictStr] | None = None
