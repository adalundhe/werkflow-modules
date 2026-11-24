from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_crawler import GlueCrawler


class GlueBatchGetCrawlersResponse(BaseModel):
    Crawlers: list[GlueCrawler] | None = None
    CrawlersNotFound: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
