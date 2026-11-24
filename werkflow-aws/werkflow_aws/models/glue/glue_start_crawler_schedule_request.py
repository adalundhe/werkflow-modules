from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueStartCrawlerScheduleRequest(BaseModel):
    CrawlerName: StrictStr
