from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_crawler_history import GlueCrawlerHistory


class GlueListCrawlsResponse(BaseModel):
    Crawls: list[GlueCrawlerHistory] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
