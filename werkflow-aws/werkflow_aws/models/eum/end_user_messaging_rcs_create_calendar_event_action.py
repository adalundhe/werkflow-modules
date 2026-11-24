from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EndUserMessagingRcsCreateCalendarEventAction(BaseModel):
    Text: StrictStr
    PostbackData: StrictStr
    Title: StrictStr
    StartTime: datetime.datetime | StrictStr
    EndTime: datetime.datetime | StrictStr
    Description: StrictStr | None = None
