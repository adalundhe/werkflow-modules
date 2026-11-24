from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GlueLastCrawlInfo(BaseModel):
    Status: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    LogGroup: StrictStr | None = None
    LogStream: StrictStr | None = None
    MessagePrefix: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
