from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueStopCrawlerScheduleRequest(BaseModel):
    CrawlerName: StrictStr
