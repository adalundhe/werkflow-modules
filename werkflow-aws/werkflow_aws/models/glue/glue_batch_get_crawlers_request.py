from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueBatchGetCrawlersRequest(BaseModel):
    CrawlerNames: list[StrictStr]
