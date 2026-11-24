from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LexConversationLogsDataSourceFilterBy(BaseModel):
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    inputMode: StrictStr | None = None
