from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class GlueCrawlerHistory(BaseModel):
    CrawlId: StrictStr | None = None
    State: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Summary: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    LogGroup: StrictStr | None = None
    LogStream: StrictStr | None = None
    MessagePrefix: StrictStr | None = None
    DPUHour: StrictFloat | StrictInt | None = None
