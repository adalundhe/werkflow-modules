from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueUpdateCrawlerScheduleRequest(BaseModel):
    CrawlerName: StrictStr
    Schedule: StrictStr | None = None
